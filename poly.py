
import math

print("Welcome to Polygon Area Calculator!")

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))

if sides < 3 or length <= 0:
    print("Invalid input! A polygon must have at least 3 sides.")

else:
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))

    print("Number of sides:", sides)
    print("Length of each side:", length)
    print("Area of polygon:", round(area, 2))
