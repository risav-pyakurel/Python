# Accept name and age from the user . check if the user is valid voter or not

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age>=18:
  print(f" Hello {name}, you're a valid voter")
else:
  print(f"Sorry {name}, you're still a minor")


