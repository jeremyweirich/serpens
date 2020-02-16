import ast

# import astor


def function_props(f):
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


def classify_function(class_attrs, decorators, variables, accesses):
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


def parse(p):
    with open(p) as f:
        tree = ast.parse(f.read())
    for statement in ast.walk(tree):
        if not isinstance(statement, ast.ClassDef):
            continue
        class_attrs = set()
        for f in statement.body:
            if isinstance(f, ast.Assign):
                for cs in ast.walk(f):
                    if isinstance(cs, ast.Name):
                        class_attrs.add(cs.id)
            if not isinstance(f, ast.FunctionDef):
                continue
            if f.name == "__init__":
                continue
            name, decorators, variables, accesses = function_props(f)

            current_category, new_category = classify_function(
                class_attrs, decorators, variables, accesses
            )
            if current_category == new_category:
                print(f"CORRECT: {name} should stay a {current_category} method")
            else:
                print(
                    f"CHANGE: {name} is a {current_category} method and should be a {new_category} method"
                )


if __name__ == "__main__":
    parse("sample/armus.py")
