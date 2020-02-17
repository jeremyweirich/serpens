# Serpens
Given a directory, try to convert instance -> class -> static methods.

## Motivation
Take a look at the following class:
```python
class Foo:
    bar = 10

    def instance_should_be_class(self):
        print(self.bar)

    def instance_should_be_static(self, x):
        return x ** 10

    @staticmethod
    def static_should_be_class():
        return Foo.bar

    @classmethod
    def class_should_be_static(cls, x):
        return x ** 10
```

Each of the method definitions could be improved.  For example the first method (`instance_should_be_class`) could 
be changed from an instance method to a class method, because the only use of `self` is to access a class attribute.

I recently ran into a situation at work where I discovered ~150 cases of the 3rd example above - static methods that 
refer explicitly to their class by name.  Many of these methods were identical except for the name of the class that 
they were found in.  If I could convert all of these static methods into class methods, I could move the method into 
the base class and delete a lot of duplicate code.

I wrote a quick hack using regexes and doing direct string replacements and was on my way in a few minutes, but I knew 
that the *right* way to do it was to parse the AST.  This repo is me learning how to do that.
 
## Methodology
1) Parse the file with `ast.parse()`
2) Use an `ast.Transformer` to walk the module in search of class definitions
3) For each class definition we visit, read the body and learn the class attributes
4) Walk the class and classify each method according the following logic:
     ```
    Does it use self?
        Y -> Could all uses of self be cls?
            Y -> Class
            N -> Instance
        N -> Does it use <classname>?
            Y -> Class
            N -> Static
    ```
5) For any methods that are the wrong category, save their location and the required transformation
6) Now visit each function definition and make the required changes:
    - static `->` class: 
        - change the decorator
        - add `cls` as the first argument
        - replace `<classname>` with `cls` in the body
    - class `->` static:
        - change the decorator
        - remove `cls` from the args
    - instance `->` class:
        - change the decorator
        - replace `self` with `cls` in the args
        - replace `self`/`<classname>` with `cls` in the body
    - instance `->` static:
        - change the decorator
        - remove `self` from the args


## Misc
The most helpful tool when working on this was the formatted output of `ast.dump()`.  The easiest way I could find to 
get a nicely formatted output was to save the output of `ast.dump()`, `import * from ast` to fix all the import errors,
then run black on the file.  Here's the full parse tree for the `Foo` class in the Motiviation (with the `Module` 
trimmed for readability)
```python
ClassDef(
    name="Foo",
    bases=[],
    keywords=[],
    body=[
        Assign(targets=[Name(id="bar", ctx=Store())], value=Num(n=10)),
        FunctionDef(
            name="instance_should_be_class",
            args=arguments(
                args=[arg(arg="self", annotation=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id="print", ctx=Load()),
                        args=[
                            Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="bar",
                                ctx=Load(),
                            )
                        ],
                        keywords=[],
                    )
                )
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            name="instance_should_be_static",
            args=arguments(
                args=[
                    arg(arg="self", annotation=None),
                    arg(arg="x", annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Name(id="x", ctx=Load()), op=Pow(), right=Num(n=10)
                    )
                )
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            name="static_should_be_class",
            args=arguments(
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Attribute(
                        value=Name(id="Foo", ctx=Load()), attr="bar", ctx=Load()
                    )
                )
            ],
            decorator_list=[Name(id="staticmethod", ctx=Load())],
            returns=None,
        ),
        FunctionDef(
            name="class_should_be_static",
            args=arguments(
                args=[
                    arg(arg="cls", annotation=None),
                    arg(arg="x", annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Name(id="x", ctx=Load()), op=Pow(), right=Num(n=10)
                    )
                )
            ],
            decorator_list=[Name(id="classmethod", ctx=Load())],
            returns=None,
        ),
    ],
    decorator_list=[],
)
```
