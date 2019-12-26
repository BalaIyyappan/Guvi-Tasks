50.Write a program to count number of digits in a number. 
SOL:
n=int(input("Enter any number:"))
count=0
temp=n

while n!=0:
  count=count+1
  
  n=int(n/10)
  
print("Number of digits in",temp,"is",count)
