def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {'+' :add ,
        '-' : sub,
        '*': multiply,
        '/' : divide  }

# print(operations['+'](4,8))
def calculator():
    should_accumulate = True
    num1 = float(input("Enter your first number:"))
    while should_accumulate:
        
        for symbols in operations:
            print(symbols)
            
        operation_symbol = input("Pick an operation from the line above:")
        num2 = float(input("Enter your second number:"))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()