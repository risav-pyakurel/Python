# reverse string using a loop

string = input("Enter any string: ")

reversed_str = ""

for char in string:
  reversed_str = char + reversed_str

print(reversed_str)