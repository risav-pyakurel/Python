# Write a program that will give you the sum of 3 digits

def sum_of_numbers():
    digit1 = float(input("enter 1st number "))
    digit2 = float(input("Enter second number "))
    digit3 = float(input("enter 3rd number "))

    total_sum = digit1 + digit2 + digit3
    print(f"The sum of 3 digits is : {total_sum}")


sum_of_numbers()
