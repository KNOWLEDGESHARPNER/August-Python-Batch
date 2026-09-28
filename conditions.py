
# # """
# # Conditional Statements -> These are the block of code which are going to execute based 
# #                           on conditions specified.
# #                         i.e, if condition is True then condition block will execute otherwise
# #                         control will jump to next block of code to execute.

# # Supported conditions in Python

# # 1. if 
# # 2. else
# # 3. elif
# # 4. nested if
# # 5. match case  -> It will work python version >= 3.10

# # """

# # """
# # if synatx:
  
# #     if condition / expression :
# #         statement(s)

# # """

# # # x = 20

# # # # check x value is greater than 50 , if it is so print x is greater than 50.

# # # # if x > 50 :
# # # #     print(f'{x} is greater than 50')

# # # # print('we are learning if statements')

# # # # read a numbers from keyboard and check it is even or odd number
# # # """
# # # else -> we can have zero or one else block for one if block
# # # """
# # # # num = int(input('Enter a number:'))

# # # # if num % 2 == 0 :
# # # #     print(f'{num} is even')
# # # # else:
# # # #     print(f'{num} is odd')

# # # """
# # # elif -> we can have zero or more elif blocks for one if block
# # # """

# # # # read a charcter from user and check it is a vowel or consonant.
# # # # aeiou -> print it is Vowel
# # # # otherwise -> print consonant

# # ch = input('Enter a character:')

# # if ch == 'a'  or ch == 'A':
# #     print(f'{ch} is vowel')
# # elif ch == 'e' or ch == 'E':
# #     print(f'{ch} is vowel')
# # elif ch == 'i' or ch == 'I':
# #     print(f'{ch} is vowel')
# # elif ch == 'o' or ch == 'O' :
# #     print(f'{ch} is vowel')
# # elif ch == 'u' or ch == 'U':
# #     print(f'{ch} is vowel')

# # else:
# #     print(f'{ch} is consonant')

# # """
# # 4. nested condition -> having one condition inside another condition is called nested condition
# # """

# # """
# # Read a country name and age from the user and check whether the person 
# # is eligible for voting or not.
# # """ 
# # country = input('Enter your country name: ')

# # if country in ['India', 'INDIA', 'india']:#Outer condition
# #     age = int(input('Enter your age: '))
# #     if age >= 18:#Inner condition / Nested condition
# #         print(f'You are eligible for voting in {country}')
# #     else:
# #         print(f'You are minor and not eligible for voting in {country}')
# # else:
# #     print(f'You are not an Indian citizen, hence not eligible for voting in {country}')

# """
# 5. match case -> It is a new feature introduced in python version >= 3.10
#                 -> It is similar to switch case in other programming languages.
# Synatx:
#     match expression:
#         case value1:
#             statement(s)
#         case value2:
#             statement(s)
#         case value3:
#             statement(s)
#         case _:
#             statement(s)    
# """

# """
# read a day number from user and print the day name using match case.
# """
# day_no = int(input('Enter a day number: '))

# match day_no:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case 6:
#         print('Saturday')
#     case 7:
#         print('Sunday')
#     case _:
#         print('Invalid day number')

"""
Debugging -> It is a process of finding and fixing the errors in the program.
          - It shows the program execution flow.
          - it shows the variable values at each step of execution.
          - It helps to understand the program logic written by other developers.
There are multiple ways to debug a program.
in that most popular way is breakpoint debugging. 
In this we can set a breakpoint at a line of code 
and when the program execution reaches that line, it will stop 
and we can check the variable values and program flow.
"""
"""
take 3 numbers from user and print the maximum number using if else statements.
"""
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 >= num2 and num1 >= num3:
    print(f'{num1} is the maximum number')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} is the maximum number')
else:
    print(f'{num3} is the maximum number')