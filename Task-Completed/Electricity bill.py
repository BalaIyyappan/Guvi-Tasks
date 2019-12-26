39.Write a program to input electricity unit charges and calculate total electricity bill 
SOL:
unit=int(input("Enter the number of units:"))
if unit<=50:
  a=unit*0.50
elif unit<100:
  a=25+(unit-50*0.75)
elif unit>100 and unit<=250:
  a=100+(unit-100*1.20)
elif unit>250:
  a=220+(unit-150*1.50)
else:
  pass
sur=a*0.20
t=a+sur
print("The Total amount is",t,'Rs')
