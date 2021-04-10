'''
    python_coding_tips

    This coding tips script is designed to run single tips in
    the python / jupyter extension of VSCode
'''

# %%
'''
ternary conditions:
'''
condition = True
x = 1 if condition else 0


# %%
'''
underscore placeholder is better to read big numbers
'''
num1 = 100_000_000_000 
num2 = 100000000000 
x = 1 if num1 == num2 else 0

# %%
'''
short form of format:
'''
num = 1000000000 
print(f'{num:,}')
1,000,000,000
print(f'0x{num:02x}') #0x3b9aca00

# %%
'''
get actual working directory
'''
import os
print(os.getcwd())
# %%
'''
use context manager to handle ressources
'''
with open('/Users/stephan_wink/workspace_github/python_scripts/scripting/cheat_sheets/general/test.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
print(f'Words in file: {len(words)}')

# %%
'''
using the enumerate function:
'''
names = ['Corey', 'Chris', 'Dave', 'Travis']


for index, name in enumerate(names, start=1):
    print (index, name)

# %%
'''
how to do multiple list accesses with 'zip' function
'''
names = ['Peter Parker', 'Clark Kent', 'Wade Whilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for name , hero in zip(names, heroes):

    print(f'{name} is actually {hero}')

# %%
'''
How does unpacking work
'''
items = (1, 2)
print(items)

#unpacking works the following:
a, b = (1, 2)
# not using the second value use underscore: a, _ = (1, 2)
print(a)
print(b)
#assigning the rest of the tuple array to c with '*', can be combined with '_' as well: '*_'
a, b, *c = (1, 2, 3, 4, 5)
print(c)

# %%
'''
getting key and value from dictionary
'''
pers_info = {'first':'Stephan', 'last':'Wink'}
for key, value in pers_info.items():
    print(key, value)

# %%
'''
adding attributes and getting attributes dynamically from
    a class using the setattr & getattr functions
'''
class Person():
    pass

person = Person()

#person.first = 'Stephan'
#person.last = 'Wink'
#print(person.first)
#print(person.last)

first_key = 'first'
first_value = 'Stephan'

setattr(person, 'first', 'Stephan')
first = getattr(person, first_key)
print(person.first, first)

# %%
'''
inputting secrete information
'''

from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')
print('logging in ...')

# %%
'''
run python with the '-m' option
'''
#running the specific module after the '-m'
# searches the sys path for the module without .py
# e.g. python -m smtpd -c DebuggingServer -n localhost:1025

# %%
'''
learn more about modules using built in functions
'''
#import smtpd
#help(smtpd)

from datetime import datetime
print(dir(datetime)) #prints all methods and attributes of a class
print(datetime.today) #prints info of this method or attribute
print(datetime.today()) #now you can use the method

# %%
