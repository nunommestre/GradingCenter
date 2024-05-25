import os

# List of emails
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

# Path to the HW1 folder in the repo
repo_path = os.path.dirname(os.path.abspath(__file__))
hw1_folder_path = os.path.join(repo_path, "HW1")

# Create the HW1 folder if it doesn't exist
os.makedirs(hw1_folder_path, exist_ok=True)

# Create a directory for each email prefix
for email in emails:
    email_prefix = email.split('@')[0]
    directory_path = os.path.join(hw1_folder_path, email_prefix)
    os.makedirs(directory_path, exist_ok=True)

print("Directories created successfully.")
