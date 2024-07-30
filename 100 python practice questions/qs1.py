# User will input (3ages).Find the oldest one

def find_oldest_age(age1, age2, age3):
    if age1 > age2 and age1 > 3:
        return age1
    elif age2 > age1 and age2 > age3:
        return age2
    else:
        return age3


age1 = int(input("Enter age of 1st person \n"))
age2 = int(input("Enter age of 2nd person \n"))
age3 = int(input("Enter age of 3rd person \n"))

oldest_age = find_oldest_age(age1,age2,age3)

print(f"The oldest age is: {oldest_age}")

