#Diameter,radius,area of circle                
def dia(r):
  return 2*r
def cir(r):
  return 2*3.17*r
def area(r):
  return 2*3.14*r**2
r=int(input("Enter the radius of circle: "))
print('Diameter of circle:',dia(r),"\nCircumference of circle:",cir(r),'\nArea of circle:',area(r))
