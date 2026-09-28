# # """
# # functions - Functions are a way to organize code into reusable blocks. 
# #             They allow you to define a set of instructions that can be executed 
# #             whenever the function is called. 
# #             Functions can take input parameters, perform operations, 
# #             and return output values.
# # Advantages of using functions:
# # 1. Code Reusability: Functions allow you to write a piece of code once and reuse it multiple times, reducing redundancy and improving maintainability.
# # 2. Modularity: Functions help break down complex problems into smaller, 
# #                 manageable tasks, making the code easier to understand and maintain.
# # 3. Readability: Functions can improve code readability by providing meaningful names 
# #                 and encapsulating logic.
# # """

# # """
# # syntax of a function:

# # def function_name(parameters): function definition
# #     # function body 

# # function_name(arguments)  - function call

# # """

# # # def greet():#parameterless function
# # #     print('Hello, Good Evening!')

# # # greet() # function call

# # """
# # functions - Functions are a way to organize code into reusable blocks. 
# #             They allow you to define a set of instructions that can be executed 
# #             whenever the function is called. 
# #             Functions can take input parameters, perform operations, 
# #             and return output values.
# # Advantages of using functions:
# # 1. Code Reusability: Functions allow you to write a piece of code once and reuse it multiple times, reducing redundancy and improving maintainability.
# # 2. Modularity: Functions help break down complex problems into smaller, 
# #                 manageable tasks, making the code easier to understand and maintain.
# # 3. Readability: Functions can improve code readability by providing meaningful names 
# #                 and encapsulating logic.
# # """

# # """
# # syntax of a function:

# # def function_name(parameters): function definition
# #     # function body 

# # # function_name(arguments)  - function call

# # # """

# # # def greet(name):#parameterized function
# # #     print(f'Hello, {name}! Good Evening!')

# # # greet("Bob") # function call

# # # # read two numbers from user and print their sum using function

# # # def add_numbers(num1, num2):
# # #     res = num1 + num2
# # #     print(res)

# # # n1 = int(input("Enter first number: "))
# # # n2 = int(input("Enter second number: "))

# # # add_numbers(n1, n2) # function call

# # # read two numbers from user and find smallest number using function

# # def find_smallest(num1, num2):
# #     if num1 < num2:
# #         print(f"The smallest number is: {num1}")
# #     elif num2 < num1:
# #         print(f"The smallest number is: {num2}")
# #     else:
# #         print("Both numbers are equal.")

# # num1 = int(input('Enter the 1st number:'))
# # num2 = int(input('Enter the 2nd number:'))

# # find_smallest(num1 , num2)

# def calc(x,y,z):
#     print(x,y,z)

# calc(10,20,'bengaluru')

# returning a value from the function 
# we will be using return keyword 

# # create a function which takes 3 parameters and return biggest of three numbers

# def find_biggest(n1,n2,n3):
#     if n1 > n2 and n1 > n3:
#         return f'{n1} is biggest'
#     elif n2 > n1 and n2 > n3:
#         return f'{n2} is biggest'
#     else:
#         return f'{n3} is biggest'

# big = find_biggest(1000,2000,300)
# print(big)

"""
Types of parameters in function

There are mainly 5 types

1. Positional Parameter
2. Keyword Parameter
3. Default Parameter
4. Arbritary variable length parameter or args parameter
5. Keyworded arbritary variable length parameter or kwargs parameter

"""
#1. Positional Parameter - arguments are passed based on the position.
# i.e., first value will go to first parameter , second value goes to second parameter so on..

# def f1(a,b,c):
#     print(a,b,c)

# f1(10,20,30)

# 2. Keyword Parameter -> while calling function arguments are passed using parameter names.


# def f1(a,b,c):
#     print(a,b,c)

# f1(c=10,a=30,b=100)

"""
3. Default Parameter -> A function can have default value for the parameter , 
                        If caller does not pass the value for that default parameter 
                        then default value will be considered.
"""

# name = Raj , mob =7899529292 , email =raj@gmail.com , course = datascience
# name = Ram , mob =9988765432 , email =ram@gmail.com , course = Python

# def counselling(name,mob,email,course='Python'):
#     print(name,mob,email,course)

# counselling('Raj',7899529292,'raj@gmail.com','Data Science')
# counselling('Ram',9988765432,'ram@gmail.com')

"""
4. Arbritary variable length parameter or args parameter

  - a funcation parameter can accept any no. of arguments.
  - args parameter is denoted by * before the parameter name
  - Internal data type of args parameter is tuple.
"""

# def f2(*a):
#     # print(a)
#     for ele in a:
#         print(ele)
#     print(type(a))

# f2() # 
# f2(10)
# f2(10,20)
# f2(10,"Raj",True)

"""
5. Keyworded arbritary variable length parameter or kwargs parameter


  - a funcation parameter can accept any no. of Keyworded argumnets(key-value pair).
  - kwargs parameter is denoted by ** before the parameter name
  - Internal data type of kwargs parameter is Dictionary
"""

def f3(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,'=',v)


f3(name='Ashwath',mob=7899529292,email='ashubig75@gmail.com')