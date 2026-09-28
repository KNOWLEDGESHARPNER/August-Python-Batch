# from second import * # It will copies entire second module
# from first import * # It will copies entire first module 
import first as f
import second as s

f.f2() 
s.f3()
s.f4()
f.f1()

"""
1.create a arithmetic.py module and define add,sub,mul,div functions 
which are taking 2 inputs and return respective output.

2. create a calc.py module and read 2 numbers from the user.
   and call the add,sub,mul,div functions from the arithmetic.py module by passing
   inputs .
"""