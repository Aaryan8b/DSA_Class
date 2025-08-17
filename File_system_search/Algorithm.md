#  Algorithm: Recursive File Search

**Inputs:**

* `path` → the starting folder
* `filename` → the name of the file we want to find

**Output:**

* The full path(s) of the file if found

---

### Step-by-Step

1. **Start** with the folder given in `path`.

2. **List all items** (files and subfolders) inside this folder.

3. **For each item in the list:**

   1. Build the **full path** of the item (combine folder path with the item name).
   2. **Check if the item is a file:**

      * If **yes** → compare its name with `filename`.
      * If it **matches** → print “Found at:” followed by the full path.
   3. **If the item is a folder:**

      * Call the same algorithm **again** on this folder (this is recursion).

4. **When all items in the folder are checked, return to the parent folder** (the function call that opened this folder).

5. **Continue** the search in the parent folder with the **next item**.

6. The process **ends when all folders and subfolders have been checked**.

---

###  Key Idea

* Files → check name, print if match.
* Folders → search inside them using recursion.
* When a folder is done → automatically return to the parent and continue.
