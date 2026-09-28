"""
Loops are a fundamental programming construct that allow you to execute a block of code
multiple times. 
In Python, there are two main types of loops: for loops and while loops.
Advantages of using loops include:
1. Code Reusability: Loops allow you to write a block of code once and
   execute it multiple times, reducing code duplication.
2. Efficiency: Loops can process large amounts of data quickly and efficiently.
3. Flexibility: Loops can be used to perform complex operations that would be 
    difficult to implement without them.
"""
"""
1. While Loops: A while loop repeatedly executes a block of code as long as a 
                specified condition is true.
    synatx:
        while condition:
            # code block to be executed
            statement(s)
    
"""
# print numbers from 1 to 10 using while loop
#o/p -> 1,2,3,4,5,6,7,8,9,10
"""
3 main parts of loops
    1. Initialization: decided on my first value of the output.
    2. Condition:It is decided based on the ending ouptut value.
    3. Update: It is decided based on the output values pattern
"""

# num = 1  # Initialization

# while  num <= 10:  # Condition
#     print(num,end=' ')  # Code block to be executed
#     num += 1  # Update

# print numbers from 10 to 1 using while loop
# o/p -> 10,9,8,7,6,5,4,3,2,1

# num = 10  # Initialization

# while num >=1:  # Condition
#     print(num,end=' ')  # Code block to be executed
#     num -= 1  # Update


x = [10,20,30,40,50,50,60,70,80,90,100,110,120]

# print numbers from list using while loop
# o/p -> 10,20,30,40,50,50,60,70,80,90,100,110,120

pos = 0  # Initialization

while pos < len(x):  # Condition
    print(x[pos],end=' ')  # Code block to be executed)
    pos += 1  # Update