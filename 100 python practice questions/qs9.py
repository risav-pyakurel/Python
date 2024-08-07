# Write a program to find the euclidean distance between two coordinates.

import math

class Euclidean:
    def __init__(self,x,y):
        self.x= x
        self.y = y

class Distance:
    @staticmethod
    def euclidean_calculator(point1,point2):
        return math.sqrt((point2.x- point1.x)**2+ (point2.y - point1.y)**2)

point1 = Euclidean(1,2)
point2 = Euclidean(3,5)

distance = Distance.euclidean_calculator(point1,point2)

print(f"The Euclidean Distance is ({point1.x}, {point1.y}) and ({point2.x},{point2.y}) is {distance:.3f}")








