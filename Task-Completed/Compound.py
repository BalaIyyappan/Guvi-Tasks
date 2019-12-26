18. Write a program to enter P, T, R and calculate Compound Interest.
SOL:
p,n,r,t=input("Enter Principle , Number of YEAR , Interest , Time of period:").split()
p=int(p)
n=int(n)
r=float(r)
t=int(t)
ci=p*(1+r/n)*n*t
print(ci)
