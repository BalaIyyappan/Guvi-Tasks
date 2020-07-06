def perfect(x):
  count=0
  for i in range(1,x):
    if(x%i==0):
      count=count+i
  if(count==x):
    return '{}'.format(x)


n=int(input("Enter the range to find Perfect number: "))
l=[perfect(i) for i in range(1,n+1)]
result=[]
for j in l:
  if j!=None:
    result.append(j)
print(result)
