
nums= [9,21,36,12,19]
target =48


for index,values in enumerate(nums):
    print( index,values)
    if values+nums[index+1] == target:
        print(f"value is {nums[index+1]} {values}")
        break