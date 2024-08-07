## Write a program that will take user input of cost price and selling price and determine whether its a loss or a profit

CP = int(input("Enter CP :"))
SP = int(input("Enter SP :"))

if CP > SP:
    print("Loss")

elif CP < SP:
    print("Profit")

else:
    print("Neither profit nor loss")
