10. Write a program to convert days into years, weeks and days.
SOL:
days=int(input("Number of days:"))
years=int(days/365)
week=int((days%365)/7)
days=days-((years*365)+(week*7))
print("Years:",years)
print("Weeks:",week)
print("Days:",days)
