import math

# ข้อ 1: class Vehicle มี instance attributes max_speed และ mileage
#        แล้วสร้าง object เพื่อพิมพ์ค่า attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


print("=== ข้อ 1 ===")
car = Vehicle(240, 18)
print("Max speed:", car.max_speed)
print("Mileage:", car.mileage)

# ข้อ 2: class Circle มี 1 method ชื่อ calculate_circle_area

class Circle:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2


print("\n=== ข้อ 2 ===")
c = Circle()
print("Area of circle (radius 5):", round(c.calculate_circle_area(5), 2))

# ข้อ 3

class Circle3:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius


print("\n=== ข้อ 3 ===")
r = float(input("Enter the radius of the circle: "))
circle = Circle3(r)
print("Area:", round(circle.calculate_circle_area(), 2))
print("Perimeter:", round(circle.calculate_circle_perimeter(), 2))


# ข้อ 4: 

class Calculator:
    def add(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b


print("\n=== ข้อ 4 ===")
calc = Calculator()
print("10 + 5 =", calc.add(10, 5))
print("10 - 5 =", calc.subtraction(10, 5))
print("10 * 5 =", calc.multiplication(10, 5))
print("10 / 5 =", calc.divide(10, 5))
print("10 / 0 =", calc.divide(10, 0))