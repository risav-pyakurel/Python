# keep asking a number with user until they asking a number between 1 and 10

while True:
  number=int( input("Enter valuue between 1 and 10 : \n"))

  if 1 <= number <=10:
    print("Thanks")
    break
  else :
    print("Invalid number, try again")
