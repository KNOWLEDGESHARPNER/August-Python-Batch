class PrivateDemo:
    def __init__(self,name,age):
        self.__pname = name # __pname is a private instance variable
        self._age = age # _age is protected instance variable

    def __display(self):
        # print(self.__pname)
        print(self._age)

class Protected(PrivateDemo):
    def pro_disp(self):
        print(self._age)
        print(self.__pname)

# p1 = PrivateDemo('Ashwath',28)

# # p1.display()

# # Access outside the class 
# print(p1._age)
# print(p1.__pname)
        
pro1 = Protected("Ashwath",30)
# pro1.pro_disp()
pro1.__display()
        
