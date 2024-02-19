# check if all elements in a list are unique. if a duplicate is found, exit a loop and print the duplicate

items = ["apple", "banana","Orange", "apple","mango"]

unique_item = set()

for item in items:
  if item in unique_item:
    print("Duplicate: ", item)
    break
  unique_item.add(item)
