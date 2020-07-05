#min max using function
def minmax(x,y):
  if x>y:
    return "{} is Maximum\n{} is Minimum".format(x,y)
  else:
    return '{} is Maximum\n{} is Minumum'.format(y,x)
  
print(minmax(5,4))
print(minmax(1,9))
