# write a decorator that measures the time of a function takes to execute

import time

def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} ran in {end-start} time")
        return result

    return wrapper
@timer
def example_function(n):
    time.sleep(n)

example_function(4)