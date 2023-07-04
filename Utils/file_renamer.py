import os

def file_renamer(directory, pattern, new_name):
    for filename in os.listdir(directory):
        if pattern in filename:
            new_filename = filename.replace(pattern, new_name)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Usage example:
# Renames all .txt files in the current directory that contain 'old' to 'new'
file_renamer('.', 'old', 'new')
