# This cheat sheet explains how to shelve variables to files
# %%
import shelve
import os

# %% 
# shelve data to a file
var = os.path.join(os.getcwd(), 'resources', 'mydata')
shelfFile = shelve.open(var)
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# %%
# read data from a shelve file
var = os.path.join(os.getcwd(), 'resources', 'mydata')
shelfFile = shelve.open(var)
print(shelfFile['cats'])


# %%
