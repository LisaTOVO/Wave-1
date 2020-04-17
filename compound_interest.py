import math
x = int(input("Please input the amount of money: "))

a = 1.04

y1 = x * (a) ** 1
y2 = x * (a) ** 2
y3 = x * (a) ** 3

print("The amound of money at the first year will be: ", (round(y1, 2)))
print("The amound of money at the secound year will be: ", (round(y2, 2)))
print("The amound of money at the third year will be: ", (round(y3, 2)))