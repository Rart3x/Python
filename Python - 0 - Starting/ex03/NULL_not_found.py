def NULL_not_found(object : any) -> int:
    match type(object).__name__:
        case "bool":
            print(object, end=" ")
        case "int":
            print(object, end=" ")
        case "float":
            print("nan", end=" ")
        case "NoneType":
            print("None", end=" ")
        case "str":
            match object:
                case "":
                    print(type(object))
                    return 0
                case _:
                    print("Type not Found", type(object))
                    return 1

    print(type(object))
    
    return 0