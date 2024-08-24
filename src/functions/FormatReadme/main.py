import os
import sys

print('FormatReadme')

def get_directories(file_path):
    # Get the directory of the specific file
    file_directory = os.path.dirname(os.path.abspath(file_path))

    # Get the directory from which Python is being run
    current_directory = os.getcwd()

    return file_directory, current_directory

def ensure_first_line_format(file_path):
    print(f"Ensure first line:{file_path}")
    # Get the parent directory name
    parent_directory_name = os.path.basename(os.path.dirname(os.path.abspath(file_path)))
    
    # Create the required first line
    required_first_line = f"# {parent_directory_name}\n"
    
    # Read the current content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the first line is correctly formatted
    if lines and lines[0].strip() == required_first_line.strip():
        print(f"The first line is already formatted correctly: {required_first_line.strip()}")
    else:
        # If the first line is not correctly formatted, update it
        lines.insert(0, required_first_line)
        print(f"Updated the first line to: {required_first_line.strip()}")

    # Update other lines that start with a single "#"
    for i in range(1, len(lines)):  # Start from the second line
        if lines[i].strip().startswith("# ") and not lines[i].strip().startswith("## "):
            lines[i] = lines[i].replace("# ", "## ", 1)
            print(f"Updated heading: {lines[i].strip()}")

    with open(file_path, 'w') as file:
        file.writelines(lines)

def format_readme_files(directory):
    print(f'format readme files in directory {directory}')
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
            if file == "_README.md":
                ensure_first_line_format(os.path.join(root, "_README.md"))

file_path = sys.argv[0]
file_directory, current_directory = get_directories(file_path)

print(f"Directory of this file: {file_directory}")
print(f"Directory from which Python is being run: {current_directory}")

format_readme_files(os.path.join(current_directory, 'src/domains'))
