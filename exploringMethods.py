# """
# Data Structure -> It is a structured way of organizing the data .
#     Systamatic way of storing program data and efficently retreving them.

#     In python we have sequence data structures 
#     That are like list, tuple, set, string , dict etc
#     All of them internally treasted as python classes.
#     Each of these classes has their own methods in it to perform specif functionalities.

#     """
# # List methods

# x = [10,11,12,13,14,15,16,17,18,90,100]
# print(x)
# # operations on this list -> CRUD operation
# # I need to a new element into my list x to the end .
# x.append(150)
# print(x)
# # I need to add 20 in between 18,90
# x.insert(9,20)
# print(x)

# # I need to remove last element 
# print(x.pop())# default index -1 last elemnt poped out
# print(x)

# print(x.pop(2))# user provided specific index 
# print(x)

# # I want to remove 15 
# x.remove(15)
# print(x)

"""
List Comprehension Technique:
 It is a concise / easy way of creating new list from an existing list.

"""
nums = [100,101,102,103,104,105,106,107]
print(nums)
# I need to copy nums list to the new list doubled_nums 
# equalent code using normal approach 

# doubled_nums = []
# for ele in nums:
#     doubled_nums.append(ele*2)

# print(doubled_nums)

# using list comprehension we will write logic inside the list only

# List_comprehension = [expression part ,iteration part,condition part]
# doubled_nums = [ele*2  for ele in nums]
# print(doubled_nums)

# generate even numbers till 50 using list comprehension

even_nums = [num for num in range(51) if num%2==0]
print(even_nums)

institute = 'Besant Technologies'

# copy all vowels into  new list using LC.
