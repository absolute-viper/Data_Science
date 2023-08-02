def harmonicSum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonicSum(n-1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Harmonic Sum of {} terms is {}".format(num, harmonicSum(num)))
