import os
import shutil

# Define source and destination folders
source_folder = "C:/Users/dell1/Downloads" # Change this path
destination_folder = "C:/Users/dell1/Pictures/JPG_Files"  # Change this path

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source folder
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        # Full paths
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move file
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

print("All .jpg files have been moved successfully!")
