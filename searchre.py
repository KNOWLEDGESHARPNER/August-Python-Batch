# import re

# address = "Python technologies Bengaluru tech"

# res = re.search('tech',address)

# print(res)
# print(res.start())
# print(res.end())

# words = re.split('\s',address)

# print(words)

# ip = "192.168.0.10"

# cleaned_data = re.split('\.',ip)
# print(cleaned_data)

# str = "python-technologies;www.python.org;anaconda.com"

# web = re.split('\;',str)

# print(web)

# ## Sub() - used to replace the string pattern with old pattern

# # stmt = 'Bengaluru is hotter than Hyderabad'

# # new_stmt = re.sub('hotter','cooler',stmt)

# # print(new_stmt)

# stmt = 'Bengaluru_is_hotter_than_Hyderabad'

# new_stmt = re.sub('_',' ',stmt,2)

# print(new_stmt)

import re
# x = 'python technologies bangalore'

# y = re.match('tech',x)

# if y:
#     print('The string starts with tech')
# else:
#     print('The string does not starts with tech')
# # print(y)

# mob = input("enter mob number:")

# res = re.match('\d{10}',mob)

# if res:
#     print('valid mob')
# else:
#     print('Please enter 10 digit mobile no..')

x = 'python Technologies'

y = re.fullmatch('p....n',x)

print(y)