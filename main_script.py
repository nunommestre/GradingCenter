import os
import shutil
import re
import zipfile
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
ASSIGNMENT_NAME = os.getenv('ASSIGNMENT_NAME')
FULL_ASSIGNMENT_NAME = os.getenv('FULL_ASSIGNMENT_NAME')
GRADING_FOLDER_NAME = os.getenv('GRADING_FOLDER_NAME')
OUTPUT_FILE_NAME = os.getenv('OUTPUT_FILE_NAME')
TOTAL_GRADE = int(os.getenv('TOTAL_GRADE'))

# Define paths
repo_path = os.path.dirname(os.path.abspath(__file__))
assignment_folder_path = os.path.join(repo_path, 'assignments')
grading_folder_path = os.path.join(repo_path, GRADING_FOLDER_NAME)
hw1_folder_path = os.path.join(grading_folder_path, ASSIGNMENT_NAME)
output_file_path = os.path.join(hw1_folder_path, OUTPUT_FILE_NAME)

# Print paths for debugging
print(f"Repository path: {repo_path}")
print(f"Assignment folder path: {assignment_folder_path}")
print(f"Grading folder path: {grading_folder_path}")
print(f"HW1 folder path: {hw1_folder_path}")
print(f"Output file path: {output_file_path}")

emails = [
    "edward_alderman@student.uml.edu",
    "patricia_antlitz@student.uml.edu",
    "lucas_aurelio@student.uml.edu",
    "garrett_bacon@student.uml.edu",
    "nabil_barkallah@student.uml.edu",
    "sergio_barroojeda@student.uml.edu",
    "joseph_beausoleil@student.uml.edu",
    "shawn_bond@student.uml.edu",
    "john_brann@student.uml.edu",
    "ayoub_darkaoui@student.uml.edu",
    "rishabh_dhir@student.uml.edu",
    "sean_diaz@student.uml.edu",
    "adam_eltelbani@student.uml.edu",
    "sudhir_gunaseelan@student.uml.edu",
    "jonathan_kang@student.uml.edu",
    "jasmeet_kaur@student.uml.edu",
    "tejindra_khatri@student.uml.edu",
    "graham_laroche@student.uml.edu",
    "david_lee@student.uml.edu",
    "khiel_mantilla@student.uml.edu",
    "xander_mury@student.uml.edu",
    "noe_musoko@student.uml.edu",
    "hai_nguyen@student.uml.edu",
    "denzel_ohenesakyi@student.uml.edu",
    "darin_abankwa@student.uml.edu",
    "zuriel_pagan@student.uml.edu",
    "rahul_pingali@student.uml.edu",
    "ali_qattan@student.uml.edu",
    "nicole_ramirez@student.uml.edu",
    "juan_ruiz@student.uml.edu",
    "tracey_shiwala@student.uml.edu",
    "brendon_so@student.uml.edu",
    "lucas_torres@student.uml.edu",
    "kalin_toussaint@student.uml.edu",
    "andy_tran@student.uml.edu",
    "wei_wang@student.uml.edu",
    "paul_warwick@student.uml.edu",
]

# Ensure the assignment folder exists
if not os.path.exists(assignment_folder_path):
    print(f"The folder '{assignment_folder_path}' does not exist.")
    exit()

# Create the assignment folder if it doesn't exist
os.makedirs(hw1_folder_path, exist_ok=True)

# Create a directory for each email prefix
for email in emails:
    email_prefix = email.split('@')[0]
    directory_path = os.path.join(hw1_folder_path, email_prefix)
    os.makedirs(directory_path, exist_ok=True)

print("Directories created successfully.")

# Move files to the corresponding directories
email_prefix_regex = re.compile(r'_([^@]+)@')
grading_subdirectories = [d for d in os.listdir(hw1_folder_path) if os.path.isdir(os.path.join(hw1_folder_path, d))]

for filename in os.listdir(assignment_folder_path):
    file_path = os.path.join(assignment_folder_path, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    match = email_prefix_regex.search(filename)
    if match:
        email_prefix = match.group(1)
        print(f"Extracted email prefix: {email_prefix}")
        
        matched_directory = None
        for subdirectory in grading_subdirectories:
            print(f"Checking subdirectory: {subdirectory}")
            subdirectory_path = os.path.join(hw1_folder_path, subdirectory)
            print(f"Full subdirectory path: {subdirectory_path}")
            if email_prefix.startswith(subdirectory):
                matched_directory = subdirectory
                break
        
        if matched_directory:
            target_folder_path = os.path.join(hw1_folder_path, matched_directory)
            shutil.move(file_path, os.path.join(target_folder_path, filename))
            print(f"Moved file '{filename}' to folder '{target_folder_path}'.")
        else:
            print(f"No matching directory found for file '{filename}' with email prefix '{email_prefix}'.")
    else:
        print(f"No email prefix found in file name '{filename}'.")

print("File moving process completed.")

# Unzip files and remove the original zip files
for root, dirs, files in os.walk(hw1_folder_path):
    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(root, file)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(root)
            os.remove(zip_file_path)
            print(f"Unzipped and removed '{zip_file_path}'.")

print("Unzipping process completed.")

# Extract submission dates and write to the output file
with open(output_file_path, 'w') as outfile:
    outfile.write("")

for directory in os.listdir(hw1_folder_path):
    directory_path = os.path.join(hw1_folder_path, directory)
    if not os.path.isdir(directory_path):
        continue

    for filename in os.listdir(directory_path):
        if filename.startswith(f"{ASSIGNMENT_NAME}_{directory}"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith("Date Submitted:"):
                        date_submitted = line[len("Date Submitted:"):].strip()
                        with open(output_file_path, 'a') as outfile:
                            outfile.write(f"Name: {directory}\n")
                            outfile.write(f"Assignment: {FULL_ASSIGNMENT_NAME}\n")
                            outfile.write(f"Date Submitted: {date_submitted}\n")
                            outfile.write("Link: \n")
                            outfile.write(f"Grade:  /{TOTAL_GRADE}\n\n")
                        break

print("Submission dates extraction completed.")
