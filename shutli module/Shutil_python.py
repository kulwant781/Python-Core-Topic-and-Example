# Shutil python module and OS module

import shutil
import os


# shutil.copy2() method using the file copy same  meta data with date
shutil.copy2("single.py", "bewimage/pery.py")


# shutil.copy() method using the file copy 
shutil.copy("single.py", "single2.py")

# Alredy create the directory and move the files 
shutil.copy() method using the file copy 
shutil.copytree("./bewimage", "./clg")

print("shutil copy2")

# New create the directory and move the files 

source = "./bewimage"
destination = "./test"

# Remove the destination directory if it exists
if os.path.exists(destination):
    shutil.rmtree(destination)

shutil.copytree(source, destination)

print("Directory copied successfully!")

# delete the folder 
shutil.rmtree("test")

print("Directory Delete successfully!")