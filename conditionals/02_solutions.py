age = int(input("Enter the age: \n"))

day = "wednesday"

price = 12 if age >=18 else 8
if day == "wednesday" :
  price  -= 2

print("Ticket price for you is $", price)
