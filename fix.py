import ast

import astor


def _function_props(f):
    decorators = [d.id for d in f.decorator_list]
    access_locations = set()
    accesses = set()
    variables = set()

    for fs in ast.walk(f):
        if isinstance(fs, ast.Attribute):
            # self and cls show up as both accesses and names, but we want to count them as just accesses
            # save their location when we see them as accesses so we can ignore them when we see them in names
            location = (fs.lineno, fs.col_offset)
            access_locations.add(location)
            accesses.add((fs.value.id, fs.attr))
        elif isinstance(fs, ast.Name):
            location = (fs.lineno, fs.col_offset)
            if location not in access_locations:
                variables.add(fs.id)

    return f.name, decorators, variables, accesses


def _classify_function(class_attrs, decorators, variables, accesses):
    """
    Does it use self?
    Y -> Could all uses of self be cls?
        Y -> Class
        N -> Instance
    N -> Does it use cls/classname?
        Y -> Class
        N -> Static
    """
    current_category = "instance"
    if "staticmethod" in decorators:
        current_category = "static"
    elif "classmethod" in decorators:
        current_category = "class"

    if "self" in variables:
        return current_category, "instance"
    if "self" in [i[0] for i in accesses]:
        if all([variable in class_attrs for _, variable in accesses]):
            return current_category, "class"
        return current_category, "instance"
    if accesses:
        return current_category, "class"
    return current_category, "static"


class ToClass(ast.NodeTransformer):
    def __init__(self, class_name):
        self.class_name = class_name

    def visit_Name(self, node):
        if node.id == "self" or node.id == self.class_name:
            node = ast.copy_location(ast.Name(id="cls", ctx=ast.Load()), node)
        return self.generic_visit(node)


class Serpens(ast.NodeTransformer):
    def __init__(self, *args, **kwargs):
        super(Serpens, self).__init__(*args, **kwargs)
        self.instance_to_static = set()
        self.instance_to_class = set()
        self.class_to_static = set()
        self.static_to_class = set()
        self.class_name = None

    def visit_ClassDef(self, node):
        class_attrs = set()
        self.class_name = node.name
        for f in node.body:
            if isinstance(f, ast.Assign):
                for cs in ast.walk(f):
                    if isinstance(cs, ast.Name):
                        class_attrs.add(cs.id)
            if not isinstance(f, ast.FunctionDef):
                continue
            if f.name == "__init__":
                continue
            name, decorators, variables, accesses = _function_props(f)
            current_category, new_category = _classify_function(
                class_attrs, decorators, variables, accesses
            )

            function_location = (f.lineno, f.col_offset)
            if current_category == "instance":
                if new_category == "static":
                    self.instance_to_static.add(function_location)
                elif new_category == "class":
                    self.instance_to_class.add(function_location)
            elif current_category == "class" and new_category == "static":
                self.class_to_static.add(function_location)
            elif current_category == "static" and new_category == "class":
                self.static_to_class.add(function_location)

        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        loc = (node.lineno, node.col_offset)
        if loc in self.static_to_class:
            print(
                f"Converting {self.class_name}.{node.name} at {loc} from static > class"
            )
            args = node.args
            args.args = [ast.arg(arg="cls", annotation=None)] + [
                i for i in node.args.args if i.arg != "self"
            ]
            node = ToClass(self.class_name).visit(node)
            node = ast.copy_location(
                ast.FunctionDef(
                    name=node.name,
                    args=args,
                    body=node.body,
                    decorator_list=[ast.Name(id="classmethod", ctx=ast.Load())],
                    returns=node.returns,
                ),
                node,
            )
        if loc in self.class_to_static:
            print(
                f"Converting {self.class_name}.{node.name} at {loc} from class > static"
            )
            args = node.args
            args.args = [i for i in node.args.args if i.arg != "cls"]
            node = ast.copy_location(
                ast.FunctionDef(
                    name=node.name,
                    args=args,
                    body=node.body,
                    decorator_list=[ast.Name(id="staticmethod", ctx=ast.Load())],
                    returns=node.returns,
                ),
                node,
            )
        if loc in self.instance_to_class:
            print(
                f"Converting {self.class_name}.{node.name} at {loc} from instance > class"
            )
            args = node.args
            args.args = [ast.arg(arg="cls", annotation=None)] + [
                i for i in node.args.args if i.arg != "self"
            ]
            node = ToClass(self.class_name).visit(node)
            node = ast.copy_location(
                ast.FunctionDef(
                    name=node.name,
                    args=args,
                    body=node.body,
                    decorator_list=[ast.Name(id="classmethod", ctx=ast.Load())],
                    returns=node.returns,
                ),
                node,
            )
        if loc in self.instance_to_static:
            print(
                f"Converting {self.class_name}.{node.name} at {loc} from instance > static"
            )
            args = node.args
            args.args = [i for i in node.args.args if i.arg != "self"]
            node = ast.copy_location(
                ast.FunctionDef(
                    name=node.name,
                    args=args,
                    body=node.body,
                    decorator_list=[ast.Name(id="staticmethod", ctx=ast.Load())],
                    returns=node.returns,
                ),
                node,
            )
        return self.generic_visit(node)


def decorator_fix(p, dryrun=False):
    with open(p) as f:
        tree = ast.parse(f.read())
    node = Serpens().visit(tree)
    if not dryrun:
        with open(p, "w") as f:
            f.write(astor.to_source(node))


if __name__ == "__main__":
    decorator_fix("samples/inplace.py", dryrun=True)

    with open("samples/before.py") as f:
        tree = ast.parse(f.read())
    node = Serpens().visit(tree)
    with open("samples/after.py", "w") as f:
        f.write(astor.to_source(node))
