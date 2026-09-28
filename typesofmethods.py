class School:
    city = "Bengaluru" # class variable

    def __init__(self,name):
        self.name = name

    def display(self):# instance method
        print(self.name)
        print(f'{School.city} this is from instance method' )

    @classmethod
    def cm(cls):
        print(cls)
        print(f'{School.city} this is from class method')
        print(cls.city)
        # print(self.name)

    @staticmethod
    def sm(x,y):
        res = x +y
        print(res)
        print(School.city)

s1 = School("ABC School")
s1.display()
School.cm()
School.sm(100,200)