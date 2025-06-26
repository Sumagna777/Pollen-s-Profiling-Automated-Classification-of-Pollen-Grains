import os
import shutil

# Paths
dataset_dir = "dataset"
organized_dir = "dataset_organized"

# Create organized directory
os.makedirs(organized_dir, exist_ok=True)

# Loop through images in dataset
for filename in os.listdir(dataset_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Extract class name (everything before the "_")
        class_name = filename.split("_")[0]

        # Create class folder inside organized_dir
        class_dir = os.path.join(organized_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)

        # Move file into the class folder
        src = os.path.join(dataset_dir, filename)
        dst = os.path.join(class_dir, filename)
        shutil.copy2(src, dst)  # Use copy2 to preserve metadata

print("✅ Dataset organized into folders by class.")
