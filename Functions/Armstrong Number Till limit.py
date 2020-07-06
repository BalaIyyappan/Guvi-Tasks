
def armstrong(x):
  x1=x
  temp=0
  while x!=0:
    t=x%10
    temp=temp+t**3
    x=x//10
  if x1==temp:
    return '{}'.format(x1)

n=int(input("Enter the range to find Armstrong number: "))
l=[armstrong(i) for i in range(1,n+1)]
result=[]
for j in l:
  if j!=None:
    result.append(j)
print(result)
