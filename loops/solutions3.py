# print the multiplication table for a given number upto 10, but skip the 5th iteration

number = int(input("Enter the number : \n"))

for i in range (1,11):
  if i ==5:
    continue
  print(number, 'x', i, '=', number *i)


