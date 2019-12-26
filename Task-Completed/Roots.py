35.Write a program to find all roots of a quadratic equation. 
SOL:
from math import sqrt
side1=float(input('Enter 1st side of a triangle:'))
side2=float(input('Enter 2nd side of a triangle:'))
side3=float(input('Enter 3rd side of a triangle:'))

d=side2*side2-(4*side1*side3)
if d>0:
  r1=(-side2+sqrt(d))/(2*side1)
  r2=(-side2*sqrt(d))/(2*side1)
  print("Roots are",r1,r2)
elif d==0 :
  r1=-side2/(2*side1)
  
  print("Roots are Root1=Root2",r1)
else:
  r=-side2/(2*side1)
  i=sqrt(-d)/(2*side1)
  print("Real and imaginary parts are",r,i)
  
