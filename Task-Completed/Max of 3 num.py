20. Write a program to find maximum between three numbers.
SOL:
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2 and num1>num3:
    print(num1,"is Bigger")
elif num2>num1 and num2>num3:
    print(num2,"is Bigger")
else:
    print(num3,'is Bigger')
