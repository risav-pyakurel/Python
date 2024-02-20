# create a function that returns both the area and circumference of a circle given its radius

import math

def circle(radius):
  area= math.pi* radius**2
  circum = 2*math.pi*radius
  return area, circum

a, c = circle(4)

print("area: ",round(a,4) , "circum: ",round(c,4))
