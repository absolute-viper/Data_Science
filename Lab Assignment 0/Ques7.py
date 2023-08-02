import math

a, b, c = map(int, input("ax^2 + bx + c, enter values of a,b,c: ").split())
d = math.pow(b, 2) - (4 * a * c)
sol1 = (-b + math.sqrt(d)) / (2 * a)
sol2 = (-b - math.sqrt(d)) / (2 * a)
print("The solutions for the equation {}x^2 + {}x + {} are {} and {}".format(a, b, c, sol1, sol2))
