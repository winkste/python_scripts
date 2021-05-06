#This cheat sheet explains several functions to handle files in python
#%%
import os

#%%
print('current working path: ' + os.getcwd())

print('absolute path: ' + os.path.abspath('.'))

print('is path absolute ? ' + str(os.path.isabs('.')))
# %%
print('relative path: ' + os.path.relpath('.'))
# %%
print('path name  of a file-path construct: ' + os.path.dirname(__file__))

print('file name of a file-path construct: ' + os.path.dirname(__file__))
# %%
# How to join a path structure always OS system conform
var = os.path.join(os.getcwd(), 'temp', 'file.txt')
print(var)

#This can also be splitted again
print(os.path.split(var))

# %%
# Calculating the size of a folder
print(os.path.getsize(os.getcwd()))

# List all elements of a folder
print(os.listdir(os.getcwd()))

# %%
# Check path validity
print(os.path.exists((os.getcwd())))

print(os.path.isdir(os.getcwd()))

print(os.path.isfile(os.getcwd()))

# %%
# Reading a text file into a string
path = os.path.join(os.getcwd(), 'resources', 'file.txt')
f = open(path)
print(f.read())
f.close()

# Reading a text file into a list
f = open(path)
print(f.readlines())
f.close()
# %%
# Writing to a text file
path = os.path.join(os.getcwd(), 'resources', 'textfile.txt')
f = open(path, 'w')
f.write('Hello World!')
f.close()
# %%
# File organization
import shutil

# Copy file from source to destination (including file name change)
shutil.copy(from_path, to_path)

# Moving the file from source to destination (including file name change)
shutil.move(from_folder, to_folder)

# Walk a folder and print all sub folder names and files
for folder_name, sub_folders, file_names in os.walk(base_folder):
    print('current folder:' + folder_name)

    for sub_folder in sub_folders:
        print('subfolder of': folder_name + ':' + sub_folder)
    
    for file_name in file_names:
        print('files in ' + folder_name + ':' + file_name)

# %%
# save deleting files and folders
import send2trash

send2trash.send2trash(file_name_path)

# %% creating and adding files to a zip file
import zipfile
newZip = zipfile.ZipFile('./resources/new.zip', 'w')
newZip.write('./resources/file.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
# %%

# %% read a compressed file with the zifile module
import zipfile

exampleZip = zipfile.ZipFile('./resources/new.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('resources/file.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.extractall('./resources/test')
exampleZip.close()


