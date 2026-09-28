class Student:
    def study(self,sub):
        print(f'Studying....{sub}')

    def take_exam(self,date,venue):
        print(f'Taking exam on {date} at {venue}')

# syntax: obj_var  = classname()

s1 = Student()

s1.study('Python OOPS')
s1.take_exam('16-09-2026','Beasnt BTM')


