import math
num = int(input("Enter a number:"))
n = num
result = 0
while num:
    temp = num % 10
    num = num // 10
    result += math.pow(temp, 3)
if int(result) == n:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
