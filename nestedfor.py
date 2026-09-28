"""
nested for loop -> having for loop inside another for loop

"""

# for i in range(1,11):# outer loop 
#     for j in range(1,11): # inner llop / nested loop
#         print(f'{i}x{j}={i*j}')
#     print()
    
# read a number from user and check it is prime or not

# num = int(input('Enter a number:'))

# for i in range(2,num):
#     if num%i == 0:
#         print('Not prime')
#         break

# else:
#     print('Prime')

# # write a program to find the prime numbers between 2 to 100 using nested for loop
# cnt = 0
# for num in range(2,101):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         print(num)  
#         cnt += 1
# print(f'Total prime numbers between 2 to 100 are: {cnt}')

# read a number from user and print the pattern as below
# i/p -> 5
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# num = int(input('Enter a number:'))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# read a number from user and print the pattern as below
# i/p -> 6
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""