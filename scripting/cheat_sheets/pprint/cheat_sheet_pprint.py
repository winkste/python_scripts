#import from standard library
import pprint

#generate dictionaries or list
d = {'Tim' : 1, 'Struppi' : 2, 'Any' : 3}
l = [1,2,3,4,5,6]

#prints the data object to the console
pprint.pprint(l)
pprint.pprint(d)

# here the formated print with a variable name to console, could be
# also a python data file for later reuse
print('d1 = ' + pprint.pformat(d))
print('l2 = ' + pprint.pformat(l))



