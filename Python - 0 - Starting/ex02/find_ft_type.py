def all_thing_is_obj(object: any) -> int:
    match type(object).__name__:
        case "str":
            print(object, "is in the kitchen", ":", type(object))
        case "double":
            print("Type not found")
        case "float":
            print("Type not found")
        case "int":
            print("Type not found")
        case "None":
            print("Type not found")
        case _:
            print(type(object).__name__.capitalize(), ":", type(object))
    return 42
