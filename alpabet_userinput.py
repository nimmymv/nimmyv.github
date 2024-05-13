user_input= (input("enter alpabet:"))
if user_input.islower():
    for i in range(ord(user_input),ord('z')+1):
        print(chr(i))
elif user_input.isupper():
    for j in range (ord(user_input),ord('Z')+1):
        print(chr(j))
else:
    print("invalid input")
