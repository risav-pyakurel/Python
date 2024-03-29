# create an electric carf class that inherits from the car class and has an additional attribute battery_size.


class Car:
  def __init__(self, brand,model): 
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"
    

class Electriccar(Car): #inheritance
  def __init__(self,brand, model , battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

my_tesla = Electriccar("BYD", "Model Dolphin","85 KwH")
print(my_tesla.model)
print(my_tesla.full_name())


# my_car= Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)

