"""
def sum(arg1,arg2):
    if type(arg1) != type(arg2):
        return 
    print(arg1 + arg2)

sum(14.66, 56.77)
sum('hello', 'world')
sum("hello", 45)
"""
'''
# default arguments *args and **kwargs

#using *args
def student(name, age, *marks):
    print("name: ", name )
    print('age', age)
    #print("marks", marks)
    for x in marks:
        print(x)

student('risav', 22, 55, 66, 78, 66, 89)
'''
# using **kwargs

def student(name, age, **marks):
    print("name: ", name )
    print('age', age)
    #print("marks", marks)
    for key,value  in marks.items():
        print(key,'', value)

student('risav', 22, AI=55, CN=66, OS=78,  TOC=66, OOP=89)
