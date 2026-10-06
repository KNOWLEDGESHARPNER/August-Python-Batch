
# # m1 = lambda x : x ** 2

# # print(type(m1))
# # res=m1(10)
# # print(res)

# # # create a lambda functuion which accepts 2 numbers and returns product .

# # product = lambda num1,num2 : num1 * num2

# # print(product(10,5))

# # # create a lambda function to find biggest of two numbers

# # big = lambda n1 , n2 :f'{n1} is biggest'  if n1 > n2  else f'{n2} is biggest'

# # print(big(1000,200))

# ## Function callback -> passing function as argument to another function

# def f1(fun):
#     res = fun(100)# func call of f2
#     print(res)

# # def f2(num): 
# #     return num * 2
# # f2 = lambda num: num * 2

# f1(lambda num : num* 2)

# Filter()

# x = [10,11,12,13,14,15]

# # print even numbers 

# even = list(filter(lambda i: i%2==0,x))
# print(even)

# map() -> 

x = [100,200,300,400,500]

# get 50% of the x list elements

res = tuple(map(lambda i:i/2,x))

print(res)