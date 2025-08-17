
# Problem:

'''
"File System Search Engine"

Imagine you are building a search tool for a file system (like how Windows Search or find in Linux works).

You have:
A directory tree (folders can have subfolders and files).
Each file has a name.

Your task:
Search for a given file name in the directory tree.
Use recursion to traverse subfolders (DFS style).
Use iteration to keep track of files found and their full paths.
Optimize with a good algorithm so search is fast for large file systems (think pruning unnecessary branches).

'''

#Algorithm

'''

#Inputs:
* `path` → the starting folder
* `filename` → the name of the file we want to find

#Output:
* The full path(s) of the file if found


1. Start with the folder given in `path`.

2. List all items inside this folder.

3. For each item in the list:

   1. Build the full path of the item (combine folder path with the item name).
   2. Check if the item is a file:
      * If **yes** → compare its name with `filename`.
      * If it **matches** → print “Found at:” followed by the full path.
   
   3. If the item is a folder:
      * Call the same algorithm **again** on this folder (this is recursion).

4. When all items in the folder are checked, return to the parent folder (the function call that opened this folder).

5. Continue the search in the parent folder with the next item.

6. The process ends when all folders and subfolders have been checked.

---

Key Idea

* Files → check name, print if match.
* Folders → search inside them using recursion.
* When a folder is done → automatically return to the parent and continue.


'''

# IN One-line

'''
“For each item here: if it is the file I want, report it; if it is a folder, search inside it the same way.”
'''





import os

def linear_search(path, filename):
    #list stuffs in the current directory
    folder=os.listdir(path)
    for item in folder:
        fullpath=os.path.join(path,item)
        if os.path.isdir(fullpath): #check full path, not filename
            
            linear_search(fullpath,filename) 
        elif os.path.isfile(fullpath):
            if item==filename:
                print("Found at: ", fullpath)

path=input("Base folder or starting path: ")           
filename=input("Enter the filename to search it: ")

linear_search(path, filename)


