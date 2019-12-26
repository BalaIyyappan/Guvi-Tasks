34.Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 
SOl:
side1=int(input('Enter 1st side of a triangle:'))
side2=int(input('Enter 2nd side of a triangle:'))
side3=int(input('Enter 3rd side of a triangle:'))


if side1==side2 and side2==side3:
  print("Triangle is Equilateral")
elif side1==side2 or side2==side3 or side3==side1 :
  print("Triangle is isosceles")
elif side1!=side2 and side2!=side3 and side3!=side1:
  print("Triangle is scalene")
else:
  print("It is not a triangle")
