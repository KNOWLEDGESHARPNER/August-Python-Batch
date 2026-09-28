"""
Types of variables:
1. Local Variables -> These are declared / created inside the functions
                      They are only accessed inside the declared function.  
2. Global Variables ->These are declared / created outside the functions.
                      They can be accessed anywhere in the program.
"""

"""
globals() -> It is a predefined function which is used to access global variables
             inside the local section whenever global and local variables names are same.

"""
x = 10 #GV
y = 20 #GV

def f1(a,b,c):#LV
    x = 100 #LV
    z = 200 #LV
    print(a,b,c)
    print(z)
    print(x)# This will print 100
    print(y)
    print(globals()['x'])#GV X value



f1(111,222,333)

# print(globals())

# print(y)