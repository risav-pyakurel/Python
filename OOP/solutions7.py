# add a static method to the car class that returns a general description of a car

class Car:
  total_car =0 

  def __init__(self, brand,model): 
    self.brand = brand
    self.model = model
    Car.total_car +=1

  def full_name(self):
    return f"{self.brand} {self.model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def general_description():
    return "Car are four wheeler"

class Electriccar(Car): #inheritance
  def __init__(self,brand, model , battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def fuel_type(self):
      return "Electric Charge"

my_tesla = Electriccar("BYD", "Model Dolphin","85 KwH")

print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
# print(safari.general_description())

print(Car.general_description())