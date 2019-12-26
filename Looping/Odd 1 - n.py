48:Write a program to find sum of all odd numbers between 1 to n. 
SOL:
n=int(input("Enter any number:"))
i=1
s=0
while i<=n:
  if i%2!=0:
    s=s+i
  i=i+1
print(s)
