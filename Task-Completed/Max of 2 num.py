19. Write a program to find maximum between two numbers.
SOL:
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1>num2:
    print(num1,"Num 1 is great")
elif num1==num2:
    print(num2,"Equal")
else:
    print(num2,"Num 2 is great")
