# modify the car class to encapsulate the brand attibute, making it private, and provide a getter method for it
class Car:
  def __init__(self, brand,model): 
    self.__brand = brand
    self.model = model
  
  def get__brand(self):
    return self.__brand + "!"

  def full_name(self):
    return f"{self.__brand} {self.model}"
    

class Electriccar(Car): #inheritance
  def __init__(self,brand, model , battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

my_tesla = Electriccar("BYD", "Model Dolphin","85 KwH")

print(my_tesla.get__brand()))
