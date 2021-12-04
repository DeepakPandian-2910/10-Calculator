print("CALCULATOR:")
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    num1 = float(input("Enter first number: "))
    for symbol in operation:
        print(symbol)
    end = False
    while not end:
        operation_symbol = input("Enter the operation symbol: ")
        num2 = float(input("Enter next number: "))
        function = operation[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        decision = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ")
        if decision == 'y':
            num1 = answer
        else:
            end = True
            calculator()
calculator()
