21. Write a program to check whether a number is negative, positive or zero.
SOL:
num=input("Enter any number:")
if num=='0':
    print(num,"is ZERO")
elif '-' in num:
    print("Negative Number")
else:
    print("Positive Number")
