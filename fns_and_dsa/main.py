from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
    if num2==0 and operation == 'divide':
        print("Second Number should not be 0")
    else:
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()