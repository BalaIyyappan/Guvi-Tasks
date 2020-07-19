n=int(input())
l=list(map(int,input().split()))
r=[]
d=n//2
o=1
e=0
for i in range(d+1):
  if i<d:
    r.append(l[o])
    # print(o,e)
    r.append(l[e])
    o=o+2
    e=e+2
  elif len(l)%2!=0:
    # print(o-1)
    r.append(l[o-1])
  else:
    pass
for j in r:
  if j!=r[-1]:
    print(j,end=" ")
  else:
    print(j)
