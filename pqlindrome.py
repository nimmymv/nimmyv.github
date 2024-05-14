def pal(number):
    return number == number[:: -1]
n=input("enter number:")
if pal(n):
    print("palindrome")
else:
    print("not a palindrome")

