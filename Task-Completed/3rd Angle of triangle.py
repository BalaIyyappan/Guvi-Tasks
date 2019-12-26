13. Write a program to enter two angles of a triangle and find the third angle.
SOL:
su=180
f=int(input("First angle:"))
s=int(input("Second angle:"))
t=abs(su-(f+s))
print("Third angle:",t)
