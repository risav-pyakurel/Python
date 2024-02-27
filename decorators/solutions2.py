# create a decorator to print the function name and the values of its
# arguments everytime the function is called.

def debug(func):
  def wrapper(*args,**kwargs):
    args_value= ', '.join(str(arg) for arg in args)
    kwargs_value = ','. join(f" {k} = {v}" for k, in v in kwargs.items())
    return func(*args,**kwargs)
    print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
    return func(*args, **kwargs)
  



  return wrapper



@debug
def  greet(name, greeting="namaste"):
  print(f"{greeting}, {name}")

greet("risav", greeting="hello") 