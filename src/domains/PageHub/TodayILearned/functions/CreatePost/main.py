import os
import sys
import time
from datetime import datetime

def get_directories(file_path):
    # Get the directory of the specific file
    file_directory = os.path.dirname(os.path.abspath(file_path))

    # Get the directory from which Python is being run
    current_directory = os.getcwd()

    return file_directory, current_directory

def create_post_file(target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Generate the file name using the current timestamp
    timestamp = int(time.time())
    file_name = f"post_{timestamp}.md"
    
    # Create the full path for the new file
    file_path = os.path.join(target_directory, file_name)
    
    # Get the current time formatted as required for the Hugo date
    hugo_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')

    # Create the new file with Hugo front matter
    with open(file_path, 'w') as file:
        file.write("+++\n")
        file.write(f"date = {hugo_date}\n")
        file.write("draft: true\n")
        file.write("+++\n\n")
    
    print(f"File created: {file_path}")
    return file_path

file_path = sys.argv[0]
file_directory, current_directory = get_directories(file_path)

print(f"Directory of this file: {file_directory}")
print(f"Directory from which Python is being run: {current_directory}")

create_post_file(os.path.join(current_directory, 'src/domains/PageHub/TodayILearned/data/index/People/GavinPalmer/posts'))
