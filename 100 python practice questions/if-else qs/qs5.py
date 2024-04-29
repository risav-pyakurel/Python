# accept a year and check if it  a leap year or not

year = int(input("Please type the year: "))

if year%4 ==0:
  print(f"{year} is a leap year")
else:
  print(f"{year} isn't a leap year")