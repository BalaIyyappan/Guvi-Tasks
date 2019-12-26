24. Write a program to check whether a year is leap year or not.
SOL:
year=int(input("Enter the year:"))
if year%400==0:
  print(year,"is Leap Year")
elif(year%100==0):
  print(year,"is not a Leap Year")
elif(year%4==0):
  print(year,"is Leap Year")
else:
  print(year,"is not a Leap Year")
