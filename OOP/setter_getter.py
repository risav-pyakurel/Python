class Employee:
    employe = 'sama'
    def setName(self,name):
        self.name = name

    def getName(self):
        print("The name is :" , self.name)

    def getemployee(cls):




e1 = Employee()
e2 = Employee()

e1.setName(input("enter the name: "))
e2.setName(input("enter the name: "))
e1.getName()
e2.getName()