def ispallindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    string = input("Enter a string: ")
    if ispallindrome(string):
        print("string is a palindrome")
    else:
        print("string is not a palindrome")
