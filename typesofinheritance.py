class A:
    def m1(self):
        print('I belongs to Parent class')

class B:
    def m2(self):
        print('I belongs to Child class')
class C(A,B):
    def m3(self):
        print('I belongs to C class')

# b = B()
# b.m1() # calling parent class method
# b.m2() # calling child class method

c = C()
c.m1()
c.m2()
c.m3()