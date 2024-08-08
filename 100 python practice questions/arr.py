# array = [
#     [1, 5, 6, 4],
#     [7, 3, 2],
#     [5, 4, 9],
#     [6, 7, 8, 9],
#     [9, 10, 7]]
#
# for arr_list in array:
#     if arr_list:
#         max_num = max(arr_list)
#         arr_list.remove(max_num)
#
# print("Array after removing the highest number inside an array is: \n")
#
# for arr_list in array:
#     print(arr_list)


import random

array = []
n = random.randint(1,10)

for obj in range(1,n+1):
    res = random.sample(range(1,100),random.randint(1,10))
    array.append(res)

print(array)

for arr_list in array:
    if arr_list in array:
        max_num = max(arr_list)
        arr_list.remove(max_num)

print("Array after removing the highest number inside an array is: \n")

for arr_list in array:
    print(arr_list)