def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    else:
        if num2 == 0 and operation == 'divide':
            return 0
        else:
            return num1 / num2