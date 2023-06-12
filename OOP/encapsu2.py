'''class Hello:
    def __init__(self,name):
        self.a =10
        self._b= 20
        self.__c= 30



hello= Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)  #we can use __ to make our value private'''

class Rectangle:
    def __init__(self,height, width) :
        self.__height= height
        self.__width= width
    def set_height(self,height):
        self.__height = height

    def set_height(self):
        self.__height

    def set_width(self,width):
        self.__width =width
    def set_width(self):
        self.__width
    def area(self):
        return self.__height * self.__width

    
rect1= Rectangle(45,67)
rect2= Rectangle(66,78)



print(rect1.area())

print(rect2.area())

