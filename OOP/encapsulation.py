class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color= color
    def set_speed(self,value):
        self.__speed= value

    def get_speed(self):
        return self.__speed


ford= Car(200,'red')
honda= Car(330,'blue')
audi= Car(400,'black')

ford.set_speed(300)
ford.__speed= 400 

print(ford.get_speed())
print(ford.color)

    