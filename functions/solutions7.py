#  write a function that takes variable number of arguments and returns their sum 

def sum_all(*args):
  return sum(args)

print(sum_all(1,2,5,6,74,4))
print(sum_all(1,2,5))
print(sum_all(1,2,23456,785,11))