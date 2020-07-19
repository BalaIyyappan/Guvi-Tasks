x,n=map(int,input().split())
l=list(map(int,input().split()))
t=-1
c=0
temp=n
while temp>0:
  # print(temp)
  if temp-l[t]>=0:
    c=c+1
    temp=temp-l[t]
  else:
    t=t-1
print(c)
      
