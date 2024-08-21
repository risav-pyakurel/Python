



class Bank:
    bank_name= 'NBL'
    rate_of_interest = 12.5

    @staticmethod
    def simple_interest(prin,n):
        si =(prin*n*Bank.rate_of_interest)/100
        print(si)

prin= float(input("Enter principle amount: "))
n= int(input("enter number of years: "))

Bank.simple_interest(prin,n)
