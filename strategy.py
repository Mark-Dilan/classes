class ArithmeticStrategy():
    def execute(self, num1, num2):
        pass

class AddStrategy(ArithmeticStrategy):
    def execute(self, num1, num2):
        return num1 + num2

class SubtractStrategy(ArithmeticStrategy):
    def execute(self, num1, num2):
        return num1 - num2

class MultiplyStrategy(ArithmeticStrategy):
    def execute(self, num1, num2):
        return num1 * num2

class DivideStrategy(ArithmeticStrategy):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2


class Calculator:
    def __init__(self, strategy: ArithmeticStrategy):
        if not isinstance(strategy, ArithmeticStrategy):
             raise ValueError("Invalid strategy provided.")
        self._strategy = strategy

    def set_strategy(self, strategy: ArithmeticStrategy):
         if not isinstance(strategy, ArithmeticStrategy):
             raise ValueError("Invalid strategy provided.")
         self._strategy = strategy


    def perform_operation(self, num1, num2):
        return self._strategy.execute(num1, num2)


if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    calculator = None
    operation_symbol = ""

    if choice == '1':
        calculator = Calculator(AddStrategy())
        operation_symbol = "+"
    elif choice == '2':
        calculator = Calculator(SubtractStrategy())
        operation_symbol = "-"
    elif choice == '3':
        calculator = Calculator(MultiplyStrategy())
        operation_symbol = "*"
    elif choice == '4':
        calculator = Calculator(DivideStrategy())
        operation_symbol = "/"

    if calculator:
        try:
            result = calculator.perform_operation(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

    