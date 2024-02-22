def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (+, -, *, /): ")

            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please choose from +, -, *, /")
                continue

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Cannot divide by zero! Please enter a non-zero second number.")
                    continue
                else:
                    result = num1 / num2

            print("Result:", result)

            play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for using the calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter numerical values.")
            continue

calculator()
