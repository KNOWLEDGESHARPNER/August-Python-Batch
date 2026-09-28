

try:
    a  = int(input('Enter a value:'))
    b = int(input('Enter b value:'))
    print(a/b)
except ZeroDivisionError:
    print('B value must be > 0')


print('Hello')
print('Bye')