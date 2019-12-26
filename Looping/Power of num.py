60.Write a program to find power of a number using for loop. 
SOL:
n1=int(input("Enter the number:"))
p=int(input("Enter the power:"))
s=n1
temp=1
for i in range(1,p+1):
  temp=temp*s
print('Power of',n1,'and',p,'is:',temp)
