38.Write a program to input basic salary of an employee and calculate its Gross salary .
SOL:
basic=int(input("Enter basic salary:"))
if basic<=10000:
  h=basic*0.2
  d=basic*0.8
  g=h+d+basic
  print("Gross Salary is:",g)
elif basic<=20000:
  h=basic*0.25
  d=basic*0.9
  g=h+d+basic
  print("Gross Salary is:",g)
elif basic>20000:
  h=basic*0.3
  d=basic*0.95
  g=h+d+basic
  print("Gross Salary is:",g)
  
