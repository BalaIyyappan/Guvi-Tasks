#Prime numbers in interval
def prime(x):
  
  p=[]
  for i in range(1,x+1):
    count=0
    for j in range(1,i+1):
      if(i%j==0):
        count=count+1
    if(count==2 and j!=2):
      p.append(j)
  return p

print(prime(50))
