num = int(input("Enter a number:"))
result = 0
for i in range(num):
    result += i
print("Sum upto {} is {}".format(num, result))