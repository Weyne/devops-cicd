import app, math
from app.util import validate_types, validate_permissions_user

class Calculator:
    @validate_types
    def add(self, x, y):
        return x + y
    
    @validate_types
    def substract(self, x, y):
        return x - y

    @validate_types
    @validate_permissions_user
    def multiply(self, x, y):
        return x * y

    @validate_types
    def divide(self, x, y):
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    @validate_types
    def power(self, x, y):
        return math.pow(x, y)
        
    @validate_types
    def sqrt(self, x):
        if x < 0:
            raise ValueError("Negative numbers are not allowed")
        return math.sqrt(x)
        
    @validate_types
    def log(self, x, y):
        if x < 0:
            raise ValueError("Negative numbers are not allowed")
        if y <= 0 or y == 1:
            raise ValueError("Base must be a positive number greater than 1")
        return math.log(x, y)

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
