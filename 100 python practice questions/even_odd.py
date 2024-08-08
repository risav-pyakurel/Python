# import random
#
# array =[]
#
# n = random.randint(1,6)
#
# for obj in range(n,n+1):
#     res=  random.sample(range(1,100),random.randint(1,7))
#     array.append(res)
#
# print(array)
#
# for list_arr in array:
#     if list_arr:
#         maximum_num= max(list_arr)
#         list_arr.remove(maximum_num)
#
# print("List after removing highest number: ")
#
# for list_arr in array:
#     print(list_arr)






def sort_even_odd(numbers):
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens + odds

print(sort_even_odd([5,10,11,35,20,60,93,99]))



