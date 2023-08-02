def isPrime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if isPrime(num):
        print("Number is Prime")
    else:
        print("Number is not Prime")
