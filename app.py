#!/usr/bin/env python
# app.py

# Import required libraries
import os
import zipfile
import stat



print("Warning: This program gives executable permissions to any executable files such as .sh and .py - If you dont want this remove the '# Set executable permissions on any executable files' part of this file.")

# Variables
destination_folder = os.getcwd()
extension = ".zip"
files = []

# Store every filename that has a .zip extension 
# in the files variable
for filename in os.listdir(destination_folder):
    if filename.endswith(extension):
        files.append(filename)

# Check if there are no .zip files
if files == []:
    print("There are no zip files to extract.")
    exit()

# Confirm if the user wants to continue
for item in files:
    print(item)
print("All these files will be unzipped. Are you sure?")
confirm = input("Y for yes N for no: ")
# If the user confirms
if confirm == "y":
    for file in files:
        # Create a new directory with the same name as the zip file
        dir_name = os.path.splitext(file)[0]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        # Extract the contents of the zip file into the new directory
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(dir_name)

        # Set executable permissions on any executable files
        extracted_folder_path = os.path.join(destination_folder, dir_name)
        for root, dirs, files in os.walk(extracted_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

    print("Completed extracting.")
# If the user doesn't confirm
else:
    # Exit the program
    print("Terminated.")
    exit()



# end of code