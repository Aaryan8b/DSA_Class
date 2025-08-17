import os

def search_file_recursive(current_dir, target_name, found_files=None):
    if found_files is None:
        found_files = []

    try:
        for entry in os.listdir(current_dir):
            full_path = os.path.join(current_dir, entry)
            if os.path.isdir(full_path):
                search_file_recursive(full_path, target_name, found_files)  # Recursive call
            elif entry == target_name:
                found_files.append(full_path)
    except PermissionError:
        pass  # Skip folders without access

    return found_files

a=search_file_recursive("Base_folder","secret.txt")
print(a)


# this version is chatgpt generated, this also returns the results instead of just printing it
