# class Car:
#     def __init__(self,speed,color) :
        
#         print(speed)
#         print(color)
#         self.speed= speed
#         self.color= color
#         print("the __init__ is called")


        
        
        
# ford = Car(55, 'red')
# honda= Car(88, 'grey')
# audi= Car(56,'blue')

# # ford.speed= 200
# # honda.speed= 430
# # audi.speed= 678

# # ford.color= 'red'
# # honda.color= 'black'
# # audi.color= 'grey'


# print(ford.speed)
# print(ford.color)




# # audi.speed= '6799'

# # print(audi.speed)

class Rectangle:
    def __init__(self,height, width) :
        self.height= height
        self.width= width
    
rect1= Rectangle(45,67)
rect2= Rectangle(66,78)



print(rect1.height*rect1.width)

print(rect2.height*rect2.width)
