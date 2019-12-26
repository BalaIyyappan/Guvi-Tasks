54.Write a program to calculate sum of digits of a number. 
SOL:
n=int(input("Enter any number:"))
s=0
while n!=0:
  i=n%10
  s=s+i
  n=int(n/10)
print("Sum of numbers is :",s)
