# TASK 2
# CALCULATOR 

def calc():
    try:
        # Get user's choice
        choices = int(input(
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Division\n"
            "4. Multiplication\n"
            "5. Exit\n\n"
            "Select a number between 1 to 5: "
        ))

        if choices not in range(1, 6):
            raise ValueError("Invalid choice. Please select a number between 1 and 5.")

        if choices == 5:
            print("Turning Off.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choices == 1:
            result = num1 + num2
            print(f"The sum of those two numbers is: {result}")

        elif choices == 2:
            result = num1 - num2
            print(f"The subtraction of those two numbers is: {result}")

        elif choices == 3:
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
            print(f"The division of those two numbers is: {result}")

        elif choices == 4:
            result = num1 * num2
            print(f"The multiplication of those two numbers is: {result}")

    except ValueError as e:
        print(f"Invalid Input: {e}")

print("Choose Options According To Your Requirements")
calc()


