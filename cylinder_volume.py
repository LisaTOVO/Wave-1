import math
r = int(input("Please enter the radius of the cylinder: "))
h = int(input("Please enter the height of the cylinder: "))

c = math.pi * (r) ** 2
v = c * h

print("The volume of the cylinder is: ", (round(v, 1)))
print(c)