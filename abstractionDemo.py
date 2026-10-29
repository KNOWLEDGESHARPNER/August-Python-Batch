from abc import ABC,abstractmethod

class ATM(ABC):

    # abstract method must not have method body
    @abstractmethod
    def withdraw(self,amt):
        pass 

    def location(self):
        print("BTM 2nd Stage")

    @abstractmethod
    def deposit(self,amt):
        pass

# a1 = ATM()# we cant create object for abstract class
class Transaction(ATM):

    def withdraw(self, amt):
        print(f'{amt} is withdrawn...')

    def deposit(self,amt):
        print(f'{amt} is deposited...')

t1 = Transaction()
t1.withdraw(2000)
t1.location()
t1.deposit(10000)