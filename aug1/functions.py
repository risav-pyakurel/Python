# def cal_sum(a, b):
#     sum = a+b
#     print(sum)
#
#
# cal_sum(1, 2)
# cal_sum(1, 3)
#


#def cal_sum(a, b):  #parameters
#return a + b


# print(cal_sum(22, 33))
# print(cal_sum(44, 66))

#sum = cal_sum(55, 66)  #function call; a,b = arguments
#print(sum)

#
# def print_hello():
#     print("Hello")
#
#
# print_hello()


# def avg_numbers(a, b, c):
#     avg = (a + b + c) / 3
#     print(f"Average of numbers : {avg}")
#
#
# avg_numbers(33, 55, 78)
#
#
# def cal_prod(a, b):
#     return a * b
#
# cal_prod()


# cities = ['chitwan', 'kathmandu', 'lalitpur', 'bhaktapur']
# attract = ['sauraha', 'basantapur', 'patan', 'bhedasingh']
#
#
# def print_len(list):
#     print(len(list))
#
#
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
#
# print_list(attract)
# print()

# n = int(input("enter the number: "))


# def cal_fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print(fact)
#
#
# cal_fact(n)

# def converter(usd_val):
#     npr_val = usd_val * 135
#     print(usd_val, "USD=", npr_val, "NPR")
#
#
# converter(2800)
#
# num = int(input("Enter the number: "))
#
#
# def odd_even(num):
#     if num % 2 == 0:
#         print("This is even number")
#     else:
#         print("This is odd number")
#
#
# odd_even(num)

# def addItemToDictionary(itemName, quantity, itemList={}):
#     itemList[itemName] = quantity
#     return itemList
#
#
# print(addItemToDictionary('notebook', 4))
# print(addItemToDictionary('pencil', 1))
# print(addItemToDictionary('eraser', 1))


def greet(name):
    return f" Hello,{name} "


def welcoming(name):
    message = greet(name=name)
    return f" welcome to our cult, {message}"


print(welcoming("risav"))
