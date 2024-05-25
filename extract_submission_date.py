import os
import re

# Define the path to the HW1 directory
repo_path = os.path.dirname(os.path.abspath(__file__))
hw1_folder_path = os.path.join(repo_path, "HW1")
output_file_path = os.path.join(hw1_folder_path, "GUI_1_Summer_2024_HW1_Grading_New.txt")

# Ensure the HW1 folder exists
if not os.path.exists(hw1_folder_path):
    print(f"The folder '{hw1_folder_path}' does not exist.")
    exit()

# Initialize the output file
with open(output_file_path, 'w') as outfile:
    outfile.write("")

# Grade details
total_grade = 30

# Iterate over each subdirectory in the HW1 folder
for directory in os.listdir(hw1_folder_path):
    directory_path = os.path.join(hw1_folder_path, directory)
    if not os.path.isdir(directory_path):
        continue

    # Look for text files starting with "HW1_{directory_name}"
    for filename in os.listdir(directory_path):
        if filename.startswith(f"HW1_{directory}"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith("Date Submitted:"):
                        date_submitted = line[len("Date Submitted:"):].strip()
                        # Write to the output file
                        with open(output_file_path, 'a') as outfile:
                            outfile.write(f"Name: {directory}\n")
                            outfile.write("Assignment: HW1\n")
                            outfile.write(f"Date Submitted: {date_submitted}\n")
                            outfile.write("Link: \n")
                            outfile.write(f"Grade:  /{total_grade}\n\n")
                        break

print("Submission dates extraction completed.")
