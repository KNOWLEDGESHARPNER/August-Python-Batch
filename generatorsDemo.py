

# def m1():
#     yield "Hello, World!"
#     yield "This is a generator function."
#     yield "It can yield multiple values."

# res = m1()

# print(res)

# # for value in res:
# #     print(value)

# print("Access the values using next() function:")

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))  # This will raise StopIteration since there are no more values to yield.

# def counter(x):
    
#     while x>=0:
#         yield x
#         x -= 1


# num = counter(500)
# print(type(num))
# # for i in num:
# #     print(i)

# l = [i**2 for i in range(100000000000000000000000000000000000)]

# print(l)

l = (i**2 for i in range(100000000000000000000000000000000000))

print(l)

print(next(l))
print(next(l))