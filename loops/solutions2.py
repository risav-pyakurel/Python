# sum of even no upto a given number n.

number = int(input("Give the number: \n"))

sum_even = 0

for i in range(1, number+1):
  if i %2 == 0:
    sum_even +=1

print("sum of even number is : \n", sum_even)

