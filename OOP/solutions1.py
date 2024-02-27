# create a car class with attributes like brand and model. then create an instance of this class 

class Car:
  def __init__(self, brand,model): #constructor __init__
    self.brand = brand
    self.model = model



my_car= Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car.model)

