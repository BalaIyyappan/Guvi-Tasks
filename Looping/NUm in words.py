59.Write a program to enter a number and print it in words. 
SOL:
i=input("Enter the number:")
words={'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero'}
for j in i:
  print(words[j])
