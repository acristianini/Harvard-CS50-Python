def main():
    question = input("Welcome to the math interpreter, please enter an arithmetic expression in the form: x y z, where x and z are integers and y is either +, -, * or /  ").strip()
    convert(question)

def convert(n):
    equation_parts = n.split()
    num1 = float(equation_parts[0])
    operator = equation_parts[1]
    num2 = float(equation_parts[2])
    
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/" if num2 != 0:
            print(num1 / num2)
        case "/" if num2 == 0:
            print("You cannot divide by 0 ")
        case _:
            print("Please use one of the four approved arithmetic operations ")

main()

