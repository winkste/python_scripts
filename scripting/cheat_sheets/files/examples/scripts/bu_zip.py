#!/usr/local/bin/python3
# bu_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder_name):

    folder = os.path.abspath(folder_name)

    #Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip' 
        if not os.path.exists(zip_file_name):
               break
        number = number + 1
    # Create the ZIP file.
    print('Creating %s...' % (zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    
    # Walk the entire folder tree and compress the files in each folder. 
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (folder_name))
        # Add the current folder to the ZIP file. 
        backup_zip.write(folder_name)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('done...')

if __name__ == '__main__':
    backup_to_zip('/Users/stephan_wink/workspace_github/python_scripts/scripting/examples/resources')

