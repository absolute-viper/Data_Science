num = int(input("Enter a number:"))
a = 0
b = 1
count = 0
if num == 1:
    print("Fibonacci sequence upto {} : {}".format(num, a))
else:
    print("Fibonacci sequence upto {} :".format(num))
    while count < num:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
