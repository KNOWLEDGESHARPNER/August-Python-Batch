

import re 

x = "python is a programming language. python is widely used."

y = re.findall("python", x)

print(y)  # Output: ['python', 'python']

z = re.findall("[py]", x)
print(z)  # Output: ['p', 'y', 'p', 'y']

a = re.findall("[^g]", x)
print(a)  # Output: ['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', '.', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ',('p", "y", "p", "y"]

m = "python lab bangalore lb is a laab"

n = re.findall("la*b", m)
print(n)  

p= re.findall("la+b", m)
print(p)  