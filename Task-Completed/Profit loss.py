36.Write a program to calculate profit or loss. 
 SOL:
 cp=int(input("Enter the cost price"))
sp=int(input("Enter the selling price"))
p=sp-cp
l=cp-sp
if cp==sp:
  print("No profit no loss")
elif sp>cp:
  print("Profit is",p)
else:
  print("Loss is",l)
