57.Write a program to check whether a number is palindrome or not. 
SOL:
n=input("Enter any number:")
temp=n
temp=temp[::-1]
if temp==n:
  print("Number is palindrome")
else:
  print("Number is not a palindrome")
