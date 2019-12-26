37.Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
SOL:
phy=int(input("Enter mark for physics"))
che=int(input("Enter mark for Chemistry"))
mat=int(input("Enter mark for MATHS"))
bio=int(input("Enter mark for Biology"))
cse=int(input("Enter mark for CSE"))
s=phy+che+mat+bio+cse
a=int((s/500)*100)
if a<40:
  print("GRADE F")
elif a>40 and a<60:
  print("GRADE E")
elif a>=60 and a<70:
  print("GRADE D")
elif a>=70 and a<80:
  print("GRADE C")
elif a>=80 and a<90:
  print("GRADE B")
elif a>=90:
  print("GRADE A")
else:
  pass
