62.Write a program to calculate factorial of a number.
SOL:
num=int(input("Enter any number:"))
fact=1
for i in range(1,num+1):
  fact=fact*i
print('Factorial of ',num,'is:',fact)
