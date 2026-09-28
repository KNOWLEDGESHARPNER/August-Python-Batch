"""
Data Type - > It is a container / place where some data is stored.

Types of Data Types in python

we can categorize 2 types

1. None Type -> It is used to store nothing.
2. Numeric Type 
    - int -> whole numbers / plain numbers ex. 10, 200, -100 ,etc
    - float -> Numbers with decimal value . ex: 3.12 , 97.5
    - bool -> True or False 
    - complex -> them numbers with real part and imaginary part . ex: 10 + 5j
3. Sequence Data Types
    1.list
    2.tuple
    3.set
    4.string
    5.range
4. Dictionary 

"""
# age = 21 
# print(age)
# print(type(age))

# percentage = 97.5
# print(percentage)
# print(type(percentage))

# isActive = True
# print(isActive)
# print(type(isActive))

# c = 10 + 5J
# print(c)
# print(type(c))

# result = None
# print(result)
# print(type(result))

"""
input() -> It is a predefined function in python 
            which is used to read any kind of values from the user / keyboard
"""
# I need to read two number from user and perform summation of them

# num1 = int(input('Enter 1st number:'))
# print(num1)
# num2 = int(input('Enter 2nd number:'))
# print(num2)
# res = num1 + num2
# print(res)

"""
1. List -> It is a multi value container which stores multiple values in it.
          - It stores elements in ordered / sequence manner
          - List elements gets assigned with index positions start from 0 .
          - List allows us to store both homogeneous and heterogenous elements.
          - List allows us store duplicate values.
          - List elements are mutable.
          - list are created using [] or list() 
"""
# student_details = ['rishi',20,7899529292,'Python',99.5,True]

# print(student_details)
# print(type(student_details))
# # access individual elements
# print(student_details[0])
# print(student_details[-1])
# print(student_details[2:4])
# # Checking mutability / changability
# student_details[1] = 22
# print(student_details)

# nums = [10,20,10,30,40,10,50]

# print(nums)
# print(type(nums))
# print(len(nums))
# print(len(student_details))

"""
2. Tuple -> It is a multi value container which stores multiple values in it.
          - It stores elements in ordered / sequence manner
          - Tuple elements gets assigned with index positions start from 0 .
          - Tuple allows us to store both homogeneous and heterogenous elements.
          - Tuple allows us store duplicate values.
          - Tuple elements are immutable.
          - tuple are created using () or tuple() 
"""
# t = (10,20,30,40,50,10,20)
# print(t)
# print(type(t))
# print(len(t))
# # immutability / can not be changed
# print(t[0])
# #t[0] = 100  # error -> TypeError: 'tuple' object does not support item assignment

"""
  3.set -> It is a multi value container which stores multiple values in it.
            - It stores elements in unordered manner or random order manner
            - Set elements does not gets assigned with index positions.
            - Set allows us to store both homogeneous and heterogenous elements.
            - Set does not allows us store duplicate values.
            - Set elements are mutable.
            - set are created using {} or set()
"""

# s = {10,20,30,40,50,10,20}
# print(s)
# print(type(s))
# print(len(s))
# # print(s[0]) error -> TypeError: 'set' object is not subscriptable

"""
4.string -> It is a collection of characters which is used to store text data 
                enclosed in single quotes or double quotes or triple quotes.
            - string is immutable.
"""
# name = 'Besant Technologies'

# print(name)
# print(type(name))
# print(len(name))
# print(name[0])
# name[0] = 'b'  

# str1 = 'Hello'
# str2 = "Python"
# print(str1)
# print(str2)
# str3 = str1 +' ' + str2 # concatenation 
# print(str3)

"""
 5.range -> It is a predefined function in python which is used to 
            generate a sequence of numbers.

            There are 3 types of range function in python
 a. range(stop) -> It generates numbers from 0 to stop-1 with step size of 1
    ex: range(101) -> 0,1,2,3,4,5,6,7,8,9,10,...99,100.

 b. range(start,stop) -> It generates numbers from start to stop-1 with step size of 1
    ex: range(10,21) -> 10,11,12,13,14,15,16,17,18,19,20

 c. range(start,stop,step) -> It generates numbers from start to stop-1 with given step size.
    ex: range(5,51,3) -> 5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50

"""
# generate numbers from 0 to 100 using range function
# nums = set(range(101)) # 0,1,2,3,4,5,6,7,8,9,10,...99,100
# print(nums)
# print(type(nums))

# generate numbers from 10 to 20 using range function
# nums = list(range(10,21)) # 10,11,12,13
# print(nums)

# generate numbers from 5 to 50 with step size of 3 using range function
# nums = tuple(range(5,51,3)) 
# print(nums)

# generate numbers from 100 to 10 which are divisible by 5 using range function

# output: 100,95,90,85,80,75,70,65,60,55,50,45,40,35,30,25,20,15,10
# nums = list(range(100,9,-5))
# print(nums)

"""
4. Dictionary -> It stores data in the form of key value pairs.
               - Keys must be unique and values can be duplicated .
               - we will use {} or dict() to create dictionary.
"""
"""
Dictionary CRUD - Create , Read , Update , Delete 
"""
# Creating 
student_details = {
    'name' : 'Suresh',
    'reg No' : 101,
    'mob' : 7899529292,
    'course' : 'Python',
    100 : 'Emergency num',
    'name':'Ramesh'
}

print(student_details)
print(type(student_details))

# Reading the dict values 
# Print course value Python

print(student_details['course'])
# print(student_details['city'])
print(student_details[100])

# Updating / Modifying values from dictionary

student_details['mob'] = 9341702287 
print(student_details)

# Adding new key value pairs to an existing dictionary
student_details['city'] = 'Bengaluru'
print(student_details)

# Get dictionary value using dictionary get method 
print(student_details.get('pincode'))

# Prind all my keys 

print(student_details.keys())

# Print all the values
print(student_details.values())

# Empty dictionary

d = {}
print(d)
print(type(d))

d['name']= 'Ashawth'
print(d)

"""
1. create empty dictionary for storing employee details 
2. read employee details from the keyboard such as 
   ename , eage , esal , edpt ,designation

3. emplayee details put into employee dictionry
4. display employee details
"""