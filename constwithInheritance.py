# class A:
#     def __init__(self):
#         print('I am const A')
# class B(A):
#     # def __init__(self):
#     #     print('I am Child Const')
#     pass
# class C(B):
#     # def __init__(self):
#     #     print('I am C const...')
#     pass

# b1 = C()

class Vehicle:
    def __init__(self,type):
        self.type = type

    def display(self):
        print(self.type)

class Bike(Vehicle):
    def __init__(self,model,color,price):
        super().__init__('Two Wheeler')
        self.model=model
        self.color = color
        self.price = price

    def bike_info(self):
        print(b1.model)
        print(b1.color)
        print(b1.price)
        super().display()

b1 = Bike('BMW','white',400000)

# print(b1.model)
# print(b1.color)
# print(b1.price)
# print(b1.type)

b1.bike_info()