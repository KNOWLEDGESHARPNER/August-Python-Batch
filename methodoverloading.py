
class A:
    def f1(self,*x):
        print(x)

    # def f1(self,x,y):
    #     print(x + y)

a = A()

a.f1(10,20)# it working fine
a.f1(100) # error-  method overloading is not supported exolicitly it is achieved By the args concept implicitly
