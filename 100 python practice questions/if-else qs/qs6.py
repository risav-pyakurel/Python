# accept an english alphabet from user and check if it is a consonant or a vowel

alpha = input("Please give a character")

if alpha in "aeiouAEIOU":
  print(f"{alpha} is a vowel")

else:
  print(f"{alpha} is a consonant")

