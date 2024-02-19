#  compute a factorial of a number using a while loop

number= int(input("Enter a number : \n"))

factorial = 1

while number > 0:
  factorial = factorial*number
  number = number -1
  #  factorial *=number it can be also use 
  # number -= 1


print("Factorial : ", factorial)
