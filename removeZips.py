import os
import zipfile

# Define the path to the HW1 directory
repo_path = os.path.dirname(os.path.abspath(__file__))
hw1_folder_path = os.path.join(repo_path, "HW1")

# Ensure the HW1 folder exists
if not os.path.exists(hw1_folder_path):
    print(f"The folder '{hw1_folder_path}' does not exist.")
    exit()

# Iterate over each subdirectory in the HW1 folder
for root, dirs, files in os.walk(hw1_folder_path):
    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(root, file)
            # Extract the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(root)
            # Remove the original zip file
            os.remove(zip_file_path)
            print(f"Unzipped and removed '{zip_file_path}'.")

print("Unzipping process completed.")
