# create a function that accepts any number of keyword arguments and prints them in the format key : Value

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:{value}")
 


print_kwargs(name= "Risav", power = "bigtime momo eater")
print_kwargs(name= "Risav")
print_kwargs(name= "Risav", power = "bigtime momo eater", studies ="CS")