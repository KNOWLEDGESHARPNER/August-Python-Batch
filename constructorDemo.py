class PythonDeveloper:
    # Constructor is used for initilizing the object .
    # assigning data into object
    def __init__(self,name,dept,email):
        # initilaization
        self.name = name # Instance variable
        self.dept = dept # Instance variable
        self.email = email # Instance variable

    def display(self):#instance method
        print(f'Name: {self.name} , Dept: {self.dept} , Email: {self.email}')


p1 = PythonDeveloper("Ashwath","Development","Ashwath@dev.com")
p2 = PythonDeveloper("Ram","Tester","ram@test.com")

p1.display()
p2.display()
