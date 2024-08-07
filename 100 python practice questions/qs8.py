# Write  a program that will tell whether the given number is divisible by 3 & 6.


class Divisible_checker:
    def __init__(self, number):
        self.number = number

    def is_divisible_by_3_and_6(self):
        return self.number %3 == 0 and self.number % 6==0

number = int(input("Enter the number :"))

checker = Divisible_checker(number)

if checker.is_divisible_by_3_and_6():
    print(f"{number} is divisible by 3 and 6 ")

else:
    print(f"{number} is not divisible by 3 and 6")