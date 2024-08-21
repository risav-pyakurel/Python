# Given an integer x, return true if x is a palindrome, and false otherwise.

number = int(input("enter the number to check the palindrome: "))

temp_num = number

reverse_num = 0

while temp_num !=0:
    digit = temp_num % 10
    reverse_num = (reverse_num*10)+ digit

    temp_num //=10

    if number == reverse_num:
        print("true")

    else:
        print("false")