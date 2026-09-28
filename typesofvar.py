# class School:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def m2(self):
#         print(f'Accessing Instance Variables inside the class using self: {self.x}')
#         print(f'Accessing Instance Variables inside the class using self: {self.y}')

# s1 = School(10,20)
# s1.m2()
# # outside the class we can access instance variables using object reference
# print(f'Accessing Instance Variables outside the class using object reference: {s1.x}')
# print(f'Accessing Instance Variables outside the class using object reference: {s1.y}')

class Test:
    test_name = "Python"  # class variable

    def __init__(self, x, y):
        self.x = x  # instance variable
        self.y = y  # instance variable

    def display(self): #insance method
        print(Test.test_name)  # accessing class variable using class name
        
print(f'Accessing Class Variable inside the class using class name: {Test.test_name}')

t1 = Test(10, 20)
t1.display()  # accessing class variable using instance method