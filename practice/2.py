import math


print("This program computes and outputs the surface area of a right circular cone.")

r = float(input("Enter the radius of a cone: "))
h = float(input("Enter the height of a cone: "))

radical = math.sqrt(r ** 2 + h ** 2)
surface = math.pi * r * (r + radical)

print(f"The surface area is {surface:.1f}")