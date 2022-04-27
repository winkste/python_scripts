#!/usr/bin/env python
""" Automatic zipping tool.

This program is intended to do an automatic zipping of the folder which
has been handed over via clipboard or command line. To make it easy, the zipper
tool is using a preconfigured output path.

How to call this script:
python zipper.py -h
python zipper.py -p path   -> overwrites the default path
python zipper.py -> expects the folder to zip in clipboard and archives to the
                    default path.
python zipper.py -i source path -> archives input path to default path
python zipper.py -o dest path -> expects a path in the clipboard and stores
                    ot dest path
input and output can be combined and used together

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Stephan Wink"
__copyright__ = "Copyright $2022, $wshield"
__credits__ = ["Al Sweigart"]
__date__ = "2022/04/01"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "Stephan Wink"
__status__ = "Production"
__version__ = "0.0.1"


################################################################################
# Imports
import os
import zipfile
from pathlib import Path
from datetime import datetime
import shelve
import argparse
import pyperclip

################################################################################
# Variables

################################################################################
# Functions

def read_dest_location():
    """Read the destination location

    Return
    ------
    str : destination location
    """

    # restoring from shelve using the with operator
    with shelve.open("zipper_param") as para:
        if "back_path" not in para.keys():
            para["back_path"] = "/Users/stephan_wink/Downloads"
        backup_path = para["back_path"]
    return backup_path


def write_dest_location(dest_loc):
    """Writes the backup file destination location to the shelve
        parameter file.

    Parameter
    ------
    dest_loc : str, destination location
    """
    if Path(dest_loc).is_dir():
        # storing to shelve using the with operator
        with shelve.open("zipper_param") as para:
            para["back_path"] = dest_loc


def generate_backup_filename():
    """Generate the backup filename

    Return
    ------
    str : backup filename
    """

    # datetime object containing current date and time
    now = datetime.now()
    # YYmmddHMS
    dt_string = now.strftime("%Y%m%d%H%M%S")
    return "backup_" + dt_string + ".zip"


def read_source_path_from_clipboard():
    """Read the source path from the clipboard

    Return
    ------
    str : destination location
    """
    text = pyperclip.paste()
    if text is not None:
        src = Path(text)
        if not src.is_dir():
            src = None
    else:
        src = None
    return src


def zip_backup(source, destination):
    """Zips the source folder to the destination

    Parameters
    ------
    source : path, source location
    destination : path, destination location
    """
    with zipfile.ZipFile(destination, "w") as new_zip:
        # pylint: disable=unused-variable
        for folder_name, sub_folders, file_names in os.walk(source):
            for file_name in file_names:
                print(f"Zipping file: {file_name}")
                new_zip.write(Path(folder_name) / file_name, compress_type=zipfile.ZIP_DEFLATED)


def main():
    """
    Main function of the program.
    """
    source_path = None
    archive_path = None

    # handle command line arguments
    parser = argparse.ArgumentParser(description = "Zipper backup generator")
    #parser.add_argument("-e", "--emul", help="emulation mode active", action="store_true")
    parser.add_argument("-i", "--input", type=str, help="folder to backup")
    parser.add_argument("-o", "--output", type=str, help="backup location")
    parser.add_argument("-p", "--path", type=str, help="path default selection")
    args = parser.parse_args()

    if args.path:
        write_dest_location(args.path)
    else:
        if args.input:
            source_path = Path(args.input)
        else:
            source_path = read_source_path_from_clipboard()
        if source_path is not None:
            if source_path.is_dir() is not True:
                print("Input path is not valid")
                return -1
        else:
            print("Call without path in clipboard, check help")
            return -3

        if args.output:
            archive_path = Path(args.output)
            if archive_path.is_dir():
                archive_path = archive_path / generate_backup_filename()
            else:
                print("Output path is not valid")
                return -2
        else:
            archive_path = Path(read_dest_location()) / generate_backup_filename()

        # zip the path to the zip file
        if archive_path is not None and source_path is not None:
            print(f"Source folder: {source_path}")
            print(f"Backup: {archive_path}")
            zip_backup(source_path, archive_path)
            print("Backup successfully generated...")

    return 0


################################################################################
# Classes

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    main()
