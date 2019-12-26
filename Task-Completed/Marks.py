16. Write a program to enter marks of five subjects and calculate total, average and percentage.
SOL:
m1,m2,m3,m4,m5=input().split()
m1=int(m1)
m2=int(m2)
m3=int(m3)
m4=int(m4)
m5=int(m5)
s=m1+m2+m3+m4+m5
a=int(s/5)
p=(s/500)*100
print(s)
print(a)
print(p)
