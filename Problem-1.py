class Calculator:
    def __init__(self, a, b, type_of_operation):
        self.a = float(a)          # double
        self.b = float(b)          # double
        self.type_of_operation = type_of_operation  # string

    def calculate(self):
        if self.type_of_operation == "Addition":
            return self.a + self.b

        elif self.type_of_operation == "Subtraction":
            return self.a - self.b

        elif self.type_of_operation == "Multiplication":
            return self.a * self.b

        elif self.type_of_operation == "Division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not allowed"

        else:
            return "Invalid operation"


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
type_of_operation = input(
    "Enter operation (Addition / Subtraction / Multiplication / Division): "
)

calculator = Calculator(a, b, type_of_operation)
result = calculator.calculate()

print("Result:", result)
