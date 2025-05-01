"""
Title: File Renamer
Description: Rename files using a given pattern
Author: Benji377
Created: 04.07.2023
Last Updated: 01.05.2025

Usage:
    file_renamer('.', 'old', 'new')

Dependencies:
    None

Notes:
    - This script is standalone and does not require other files from the repo.
    - Adjust any parameters or constants at the top of the script as needed.
"""


import os

def file_renamer(directory, pattern, new_name):
    for filename in os.listdir(directory):
        if pattern in filename:
            new_filename = filename.replace(pattern, new_name)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Usage example:
# Renames all .txt files in the current directory that contain 'old' to 'new'
file_renamer('.', 'old', 'new')
