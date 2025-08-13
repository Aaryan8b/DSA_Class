# A program to create multiple folders and sub-folders, and text 2 files at the end

#Main concept:
'''
import os

# To create one folder

os.mkdir("my_folder")

# To create nested folders (will create parent directories too)

os.makedirs("parent_folder/child_folder/grandchild_folder", exist_ok=True)

#To make a txt file 

 for k in range(2):
            file_path = os.path.join(sub_path, f"file_{k}.txt")
            with open(file_path, "w") as f:
                f.write(f"This is file {k} inside {sub_path}\n")

'''

#Algorithm

'''
use a for loop to make parent folders in the current directory
use nested loops to make sub folders and files simultaneously
'''


import os

for i in range(3):                              #for folders
    folder_name="parentfolder"+str(i)
    os.makedirs(folder_name, exist_ok=True)     #exist_ok=True to avoid errors if directory already exists
    for j in range (2):                         #for subfolders
        subfolder_name="subfolder"+str(j)
        os.makedirs(folder_name+"/"+subfolder_name, exist_ok=True)
        for k in range(2):                      #for text files
            file_path = f"{folder_name}/{subfolder_name}/file{str(k)}.txt"
            with open(file_path, "w") as f:
                f.write(f"This is file {k} inside '{folder_name+subfolder_name}'\n ")
