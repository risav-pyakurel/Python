
# Write a program that will tell whether the number entered by the user is odd or even.
def odd_even(num):
    if num % 2 == 0:
        print("This is even number")
    else :
        print("this is odd number")

user_input = int(input(" Enter the number: "))

odd_even(user_input)