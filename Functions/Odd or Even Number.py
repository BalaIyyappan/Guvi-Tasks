#Even or odd function
def eoro(n):
  if(n%2==0):
    return "Even number"
  else:
    return "Odd number"

c=int(input("Enter any number:"))
print(eoro(c))
