32.Write a program to input angles of a triangle and check whether triangle is valid or not. 
SOL:
angle1=int(input('Enter 1st angle of a triangle:'))
angle2=int(input('Enter 2nd angle of a triangle:'))
angle3=int(input('Enter 3rd angle of a triangle:'))
s=angle1+angle2+angle3

if s==180:
  print("Triangle is valid")
else:
  print("Triangle is not valid")
