def NULL_not_found(object: any) -> int:
    match type(object).__name__:
        case "bool":
            print("Fake:", object, end=" ")
        case "int":
            print("Zero:", object, end=" ")
        case "float":
            print("Cheese: nan", end=" ")
        case "NoneType":
            print("Nothing: None", end=" ")
        case "str":
            match object:
                case "":
                    print("Empty:", type(object))
                    return 0
                case _:
                    print("Type not Found")
                    return 1

    print(type(object))

    return 0
