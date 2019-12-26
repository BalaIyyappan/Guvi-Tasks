49.Write a program to print multiplication table of any number. 
SOL:
n=int(input("Enter any number:"))
i=1

while i<=10:
  s=n*i
  print(n,'*',i,'=',s)
  i=i+1
