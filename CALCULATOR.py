def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("Select the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt the user to choose an operation
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid choice.")
        return
    
    # Display the result
    print(f"The result of {num1} {operation} {num2} is {result}")

# Call the calculator function
calculator()
