msg = ['hello', 'Alex']

match msg:
    case ["hello"]:
        print("this message says hello")
    case ["hello", name]:
        print(f"This message is a personal greeting to {name}")
    case _:
        print("The message didn’t match with anything")