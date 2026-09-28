"""
for loop -> is used to iterate the sequences 
            It is used to execute block of code for an given no.of times 

syntax:

    for iterating_var in sequence_name:
        statement(s)
"""
# for loop with list 

# x = [10,20,30,40,50]

# for ele in x:
#     print(ele)

# for loop with tuple

# t = (100,200,300,400,500,600)

# for i in t:
#     print(i,end=' ')

# working with set

# s1 = {10,20,30,40,50,60,70,80,90,100}

# for e in s1:
#     print(e,end= ' ')

# working with string

# st = 'Python Loops examples'

# for ch in st:
#     print(ch)

"""
1. Want to display sequence elements in reverse 
2. want to display sequence alternative elements
"""

# nums = [10,11,12,13,14,15,16,17,18,19,20]
# o/p -> 20,19,.....10

# for loop with range()
# numbers from 0 to 10

# for num in range(11):
#     print(num)

# for pos in range(len(nums)):
#     print(nums[pos],end=',')

# for pos in range(len(nums)-1,-1,-1):
#     print(nums[pos],end=' ')

# for i in range(0,len(nums),2):
#     print(nums[i],end=' ')

"""
marks = [95,67,89,56,78,49]
1. calculate total obtained marks of the student -> 434
2. display the percentage  - 72.33
3. display the count of subjects which are less than 60 -> 2
"""
marks = [95,67,89,56,78,49]
total = 0
cnt = 0
for score in marks:
    total += score
    if score < 60:
        cnt += 1

print(f'Total Obtained marks is:{total}')
percentage = (total/600)*100
print(f'Percentage is:{percentage}')
print(f'No. of subjects required imrovements:{cnt}')