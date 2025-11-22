import math

def calculator():
    while True:
        print("\n====== PYTHON CALCULATOR ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '8':
            print("Thank you for using the calculator!")
            break

        # Square root only needs one number
        if choice == '6':
            num = float(input("Enter number: "))
            print("Square Root =", math.sqrt(num))
            continue

        # For all other operations we need two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result =", num1 + num2)
        elif choice == '2':
            print("Result =", num1 - num2)
        elif choice == '3':
            print("Result =", num1 * num2)
        elif choice == '4':
            try:
                print("Result =", num1 / num2)
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
        elif choice == '5':
            print("Result =", num1 ** num2)
        elif choice == '7':
            print("Result =", num1 % num2)
        else:
            print("Invalid input! Please try again.")

calculator()