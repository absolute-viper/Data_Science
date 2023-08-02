import math


def isDisarium(n):
    n2 = n
    result = 0
    i = len(str(n))
    while n:
        temp = n % 10
        n = n // 10
        result += math.pow(temp, i)
        i -= 1

    if int(result) == n2:

        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if isDisarium(num):
        print("Number is a Disarium Number")
    else:
        print("Number is not a Disarium Number")
