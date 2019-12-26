22. Write a program to check whether a number is divisible by 5 and 11 or not
SOL:
num=int(input("Enter any number:"))
if num%5==0 and num%11==0:
    print(num,"is Divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")
