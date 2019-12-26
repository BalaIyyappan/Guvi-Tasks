55.Write a program to calculate product of digits of a number. 
SOL:
n=int(input("Enter any number:"))
s=1
while n!=0:
  i=n%10
  s=s*i
  n=int(n/10)
print("Sum of numbers is :",s)
