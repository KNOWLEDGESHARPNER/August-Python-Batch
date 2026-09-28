
class A:
    def m1(self,x):
        print('I am Parent m1')
        print(x)

class B(A):
    def m1(self, y):
        print('I am m1 inside Child class')
        print(y)
        super().m1('ML')

b1 = B()

b1.m1("GEN AI")
