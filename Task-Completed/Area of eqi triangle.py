15. Write a program to calculate area of an equilateral triangle.
SOL:
from math import sqrt
a=int(input("Enter the side:"))
area=(sqrt(3)/4)*a*a
print("{:.2f}".format(area))
