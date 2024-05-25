import os
import shutil
import re

# Define paths
repo_path = os.path.dirname(os.path.abspath(__file__))
assignment_folder_path = os.path.join(repo_path, "assignments")
grading_folder_path = os.path.join(repo_path, "GUI I Grading")

# Create a regular expression to extract the email prefix from the file name
email_prefix_regex = re.compile(r'_([^@]+)@')

# Ensure the assignment folder exists
if not os.path.exists(assignment_folder_path):
    print(f"The folder '{assignment_folder_path}' does not exist.")
    exit()

# Get list of all directories in the grading folder
grading_directories = os.listdir(grading_folder_path)

# Iterate over files in the assignment folder
for filename in os.listdir(assignment_folder_path):
    file_path = os.path.join(assignment_folder_path, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Search for the email prefix in the file name
    match = email_prefix_regex.search(filename)
    if match:
        email_prefix = match.group(1)
        
        # Find the matching directory
        matched_directory = None
        for directory in grading_directories:
            if email_prefix.startswith(directory):
                matched_directory = directory
                break
        
        if matched_directory:
            target_folder_path = os.path.join(grading_folder_path, matched_directory)
            # Move the file to the corresponding directory
            shutil.move(file_path, os.path.join(target_folder_path, filename))
            print(f"Moved file '{filename}' to folder '{target_folder_path}'.")
        else:
            print(f"No matching directory found for file '{filename}'.")
    else:
        print(f"No email prefix found in file name '{filename}'.")

print("File moving process completed.")
