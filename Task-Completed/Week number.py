29.Write a program to input week number and print week day. 
SOL:
week=int(input("Enter week number:"))
if week==1:
  print("Monday")
elif week==2:
  print("Tuesday")
elif week==3:
  print("Wednesday")
elif week==4:
  print("Thursday")
elif week==5:
  print("Friday")
elif week==6:
  print("Saturday")
elif(week==7):
  print("Sunday")
else:
  pass
