
#Prime or armstrong or perfect number
def prime(x):
  for i in range(1,x+1):
    count=0
    for j in range(1,i+1):
      if(i%j==0):
        count=count+1
    if(count==2 and j!=2):
      return '{} is a prime number'.format(x)
    else:
      return '{} is not a prime number'.format(x)

def armstrong(x):
  x1=x
  temp=0
  while x!=0:
    t=x%10
    temp=temp+t**3
    x=x//10
  if x1==temp:
    return '\n{} is Armstrong number'.format(x1)
  else:
    return '\n{} is not an armstrong number'.format(x1)


def perfect(x):
  count=0
  for i in range(1,x):
    if(x%i==0):
      count=count+i
  if(count==x):
    return '\n{} is a perfect number'.format(x)
  else:
    return '\n{} is not a perfect number'.format(x)

x=int(input('Enter any number:'))
print(prime(x),armstrong(x),perfect(x))
