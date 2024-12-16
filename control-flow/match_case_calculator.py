num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):.")

match operation:
    
    case "+":
        addition = num1 + num2
        print(f"Result: {addition}")
        
    case "-":
        subtract = num1 - num2
        print(f"Result: {subtract}")
        
    case "*":
        multiply = num1 * num2
        print(f"Result: {multiply}")
        
    case "/":
        if num2 == 0:
            print("You cant divide by 0!")
        else:
            divide = num1 / num2
            print(f"Result: {divide}")