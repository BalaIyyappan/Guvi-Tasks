61.Write a program to find all factors of a number. 
SOL:
num=int(input("ENter any number:"))
a=[]
for i in range(1,num+1):
  if num%i==0:
    a.append(i)
print(a)
