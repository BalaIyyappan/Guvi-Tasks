30.Write a program to input month number and print number of days in that month. 
SOL:
month=int(input('Enter the month number:1-January 2-February 3-March 4-April 5-May 6-June 7-July 8-August 9-September 10-October 11-November 12-December:'))
if month==1:
  print("It has 31 days")
elif month==2:
  print("It has 28 days")
elif month==3:
  print("It has 31 days")
elif month==4:
  print("It has 30 days")
elif month==5:
  print("It has 31 days")
elif month==6:
  print("It has 30 days")
elif month==7:
  print("It has 31 days")
elif month==8:
  print("It has 31 days")
elif month==9:
  print("It has 30 days")
elif month==10:
  print("It has 31 days")
elif month==11:
  print("It has 30 days")
elif month==12:
  print("It has 31 days")
else:
  pass
