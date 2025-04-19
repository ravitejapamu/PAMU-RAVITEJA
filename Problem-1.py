#Problem-1 (Calculator): Implement a class-based calculator that performs addition, subtraction, multiplication, and division operations.
#Create a class named Calculator.
#Define methods within the class for each operation: add, subtract, multiply, divide.
#Each method should accept two double-precision floating-point numbers as input (a and b).
#The operation type should be a string input indicating which operation to perform.
#Return the result of the calculation. Handle division by zero appropriately.


class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "Addition":
            return self.a + self.b
        elif self.operation == "Subtraction":
            return self.a - self.b
        elif self.operation == "Multiplication":
            return self.a * self.b
        elif self.operation == "Division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation"

# Example usage
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the type of operation (Addition, Subtraction, Multiplication, Division): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print(f"Result: {result}")