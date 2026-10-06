
# # nested method and returning a method

# def m1():#outer function
#     print("Inside m1")
#     def m2():# nested function
#         print("Inner method m2")
#     return m2# returning the nested function

# res=m1()# outer function call
# res()# calling the returned nested function

# custom decorator
"""
******************************************
Welcome to Python 
******************************************
"""

# def outer_decor(func):
#     def inner_decor():
#         print("*" * 40)
#         func()
#         print("*" * 40)
#     return inner_decor

# @outer_decor
# def greeting():
#     print("Welcome to Python")

# greeting()

"""
expected output: HELLO GOOD MORNING EVERYONE

"""

def outer_decor(func):
    def inner_decor(x,y):
        x = x.upper()
        y = y.upper()
        res=func(x,y)
        return res
    
    return inner_decor

@outer_decor
def str_fun(x,y):
    return x,y

a = str_fun("hello good morning", "everyone")
print(a)



def str_fun(x):
    return x
a = str_fun("HELLO GOOD MORNING EVERYONE")
print(a)

"""
add decorator for above function to split the data and store in list
expected output: ["HELLO", "GOOD", "MORNING",“EVERYONE"]

"""