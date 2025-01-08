def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    
    if operation == 'subtract':
        return num1 - num2
    
    if operation == 'multiply':
        return num1 * num2
    
    if num2==0:
        print("Second Number should not be 0")
    else:
        return num1 / num2