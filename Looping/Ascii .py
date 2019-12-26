59.Write a program to print all ASCII character with their values. 
SOL:
a=97
A=65
print("Capital letters:")
for i in range(65,91):
  print(chr(i))
print("Small letters:")
for i in range(97,123):
  print(chr(i))
