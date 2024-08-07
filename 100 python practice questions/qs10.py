## Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if (a+b+c == 180) and a!=0 and b!=0 and c!=0 :
    print ("Valid triangle")
else :
    print ("Not a valid triangle")