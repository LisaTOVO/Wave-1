m = int(input("Please enter the amount of cents: "))
t = m // 200
l = (m - (t * 200)) // 100
q = ((m - (t * 200)) - (l * 100)) // 25
d = ((m - (t * 200)) - (l * 100) - (q * 25)) // 10
n = ((m - (t * 200)) - (l * 100) - (q * 25) -(d * 10)) // 5
p = ((m - (t * 200)) - (l * 100) - (q * 25) -(d * 10) - (n * 5)) // 1

print("The current amount is: ", m, "cents")
print("There are", t, "toonies")
print(l, "loonies")
print(q, "quarters")
print(d, "dimes")
print(n, "nickels")
print("and", p, "pennies")

