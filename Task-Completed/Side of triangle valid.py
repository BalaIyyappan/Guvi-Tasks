33.Write a program to input all sides of a triangle and check whether triangle is valid or not. 
SOL:
side1=int(input('Enter 1st angle of a triangle:'))
side2=int(input('Enter 2nd angle of a triangle:'))
sidle3=int(input('Enter 3rd angle of a triangle:'))


if side1**2==(side2**2+sidle3**2) or side2**2==(side1**2+sidle3**2) or sidle3**2==(side1**2+side2**2):
  print("Triangle is valid")
else:
  print("Triangle is not valid")
