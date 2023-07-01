import os
import random
import string

# Set the folder path where you want to create the files
folder_path = "C:/Users/name/Example/randomfiles"

# Set the number of files you want to create
num_files = 200

# Set the range for file sizes (in bytes)
min_size = 10000  # Minimum file size
max_size = 10000000  # Maximum file size

# Set the range for file content length (number of characters)
min_content_length = 50  # Minimum content length
max_content_length = 500  # Maximum content length

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Generate and save the files
for i in range(num_files):
    # Generate random content for the file
    content_length = random.randint(min_content_length, max_content_length)
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=content_length))

    # Generate random file size
    file_size = random.randint(min_size, max_size)

    # Generate a random filename
    filename = f"file_{i}.txt"

    # Create the file path
    file_path = os.path.join(folder_path, filename)

    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

    # Set the file size
    os.truncate(file_path, file_size)

print(f"{num_files} files created in {folder_path}.")
