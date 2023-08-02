import math


def geometricSum(n):
    if n == 1:
        return 1
    else:
        return 1/math.pow(2, n-1) + geometricSum(n-1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Harmonic Sum of {} terms is {}".format(num, geometricSum(num)))

# Output: fibonnaci series
# Enter a number: 5