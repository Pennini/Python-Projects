from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_end = False
    while not should_end:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        repeat = input(
            f"Type 'y' to continue calculating with {answer}, or type 's' to start a new calculation or 'n' to finish calculating: "
        )
        if repeat == "y":
            num1 = answer
        elif repeat == "s":
            should_end = True
            clear()
            calculator()
        elif repeat == "n":
            should_end = True


calculator()
