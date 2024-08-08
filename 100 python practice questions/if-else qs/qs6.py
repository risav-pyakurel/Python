# accept an english alphabet from user and check if it is a consonant or a vowel
#
# alpha = input("Please give a character")
#
# if alpha in ['a','e','i','o','u', 'A','E', 'I','O','U']:
#   print(f"{alpha} is a vowel")
#
# else:
#   print(f"{alpha} is a consonant")
#


a = [1,2,3,4]

if 3 in a:
  print('3 aayo')

  array = [5, 10, 11, 35, 20, 60, 93, 99]

  # Separate even numbers and sort them
  even_numbers = sorted([x for x in array if x % 2 == 0])

  # Iterate through the original array and replace even numbers with sorted ones
  even_index = 0
  for i in range(len(array)):
    if array[i] % 2 == 0:
      array[i] = even_numbers[even_index]
      even_index += 1

  print("Array after arranging even numbers:", array)