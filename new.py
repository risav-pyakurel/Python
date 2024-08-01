# class My:
#     def __init__(self, para1, para2):
#         self.para1 = para1
#         self.para2 = para2
#
#     def show_params(self):
#         print(f" Parameter 1: {self.para1}")
#         print(f" Parameter 2: {self.para2}")
#
#     def sum_of_param(self):
#         return self.para1 + self.para2
#
#
# obj = My(para1=4, para2=7)
# obj.show_params()
# print(obj.sum_of_param())


# functions calling functions

def greet(person, first_time=False):
    if first_time:
        return "New joined??, Welcome!" + person
    return "Hello, " + person


def greet_all(people):
    for person in people:
        print(greet(person, True))


friends = ['Risav', 'Sam', 'ankit']

greet_all(friends)
