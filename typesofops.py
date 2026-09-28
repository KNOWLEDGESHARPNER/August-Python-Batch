# # # x = 10 # declaration and initialization of variable x

# # # print(x) # printing the value of variable x

# # # x = 15
# # # print(x)

# # x = 10
# # print(x)
# # x += 5 # addition assignment operator, adds 5 to the current value of x
# # print(x)
# # x -= 2
# # print(x)

# """
# 3. Relational / comparisons ops -> < , > ,<= ,>=,!=, ==    
#                 -> True or False
#         Normally to build conditions logic 
# """
# # a  = 200
# # b  = 200

# # print(a < b)
# # print(a == b)
# # print(a != b)
# # print(b <= a)

# """
#  4. Logical ops -> and , or , not
#    It is used to combine multiple conditions to get 
#    single True or False result
# """
# """
# and operator truth table

# exp1    and     exp2    result
# T       and      F       F
# F       and      T       F
# F       and      F       F
# T       and      T       T 

# or Opertator Truth Table
# exp1    or     exp2    result
# T       or      F       T
# F       or      T       T
# F       or      F       F
# T       or      T       T

# """
# # ep1 = 10
# # ep2 = 20
# # ep3 = 30

# # print(ep1 > ep2 and ep2 < ep3)

# # print(ep3 == ep1 or ep2 < ep3)

# # b = True

# # print(b)
# # print(not b)

# """
#  5. Bitwise ops -> & (bitwise and ) , | (Bitwise or)
#     - These are used to perform binary bit level operations.
#     - Especially used in networking programmings.
# """

# n1 = 5 # 0101 
# n2 = 2 # 0010

# print(n1 & n2)
# print(n1 | n2)


"""
 7.Identity ops ->  is , is not 
   - These are used to check identity of mulptiple objects .
   - They are going to compare both objects are present in 
     same membory address or not.
"""
a = 20
b = 20
print(id(a))
print(id(b))
print(a is b)
print(a is not b)