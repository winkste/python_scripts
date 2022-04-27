# %%
# Test script for zipper.py
import os
import pyperclip
import time

# Call zipper with no parameters
pyperclip.copy('NO PATH')
var = os.system("python scripts/zipper.py")
# %%
# Call zipper and setup path variable in shelve file
pyperclip.copy('NO PATH')
os.system("python scripts/zipper.py -p /Users/stephan_wink/workspace_github/python_scripts/scripting/zipper/test/")
time.sleep(2)

# Call zipper with clipboard and zip resources
pyperclip.copy('/Users/stephan_wink/workspace_github/python_scripts/scripting/zipper/test/resources')
os.system("python scripts/zipper.py")
time.sleep(2)

# Call zipper with input parameter
pyperclip.copy('NO PATH')
os.system("python scripts/zipper.py -i /Users/stephan_wink/workspace_github/python_scripts/scripting/zipper/test/resources")
time.sleep(2)

# Call zipper with input and output parameter
pyperclip.copy('NO PATH')
os.system("python scripts/zipper.py -i /Users/stephan_wink/workspace_github/python_scripts/scripting/zipper/test/resources -o /Users/stephan_wink/workspace_github/python_scripts/scripting/zipper/test/")
time.sleep(2)
# Check all zips are generated

# Delete all test zips

