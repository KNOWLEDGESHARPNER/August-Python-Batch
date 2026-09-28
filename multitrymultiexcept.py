
try:
    x =int(input('Enter a x value:'))
    print(x)
except ValueError as e:
    print(e)

try:
    nums = [10,20,30,40]
    print(nums[0])
    print(nums[1])
    print(nums[4])

except IndexError as e:
    print(e)

print('All exceptions handled sucessfully!!!')