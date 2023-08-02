def pallindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    num = input("Enter a number: ")
    if pallindrome(num):
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")
