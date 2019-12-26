17. Write a program to enter P, T, R and calculate Simple Interest.
SOL:
p,n,r=input("Enter Principle , Number of YEAR , Interest:").split()
p=int(p)
n=int(n)
r=float(r)
si=p*n*r/100
print(si)
