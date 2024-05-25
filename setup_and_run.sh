#!/bin/zsh

# Define the project directory
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Navigate to the project directory
cd "$PROJECT_DIR"

# Install required Python packages
pip3 install -r requirements.txt

# Run the main Python script
python3 main_script.py
