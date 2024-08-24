import os
import sys

print('FormatReadme')

def get_directories(file_path):
    # Get the directory of the specific file
    file_directory = os.path.dirname(os.path.abspath(file_path))

    # Get the directory from which Python is being run
    current_directory = os.getcwd()

    return file_directory, current_directory

def rename_readme_files(directory):
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "README.md":
                # Create the full path to the file
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, "_README.md")
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")


file_path = sys.argv[0]
file_directory, current_directory = get_directories(file_path)

print(f"Directory of this file: {file_directory}")
print(f"Directory from which Python is being run: {current_directory}")

rename_readme_files(f'{current_directory}/src/domains')
