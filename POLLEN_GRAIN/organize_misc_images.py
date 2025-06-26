import os
import shutil

dataset_path = "dataset"

# Create folder if not exists
senegalia_folder = os.path.join(dataset_path, "senegalia")
urochloa_folder = os.path.join(dataset_path, "urochloa")
os.makedirs(senegalia_folder, exist_ok=True)
os.makedirs(urochloa_folder, exist_ok=True)

# Move senegalia images
for file in os.listdir(dataset_path):
    if file.lower().startswith("senegalia") and file.lower().endswith(".jpg"):
        shutil.move(os.path.join(dataset_path, file), os.path.join(senegalia_folder, file))

# Move urochloa images
for file in os.listdir(dataset_path):
    if file.lower().startswith("urochloa") and file.lower().endswith(".jpg"):
        shutil.move(os.path.join(dataset_path, file), os.path.join(urochloa_folder, file))

print("✅ All stray senegalia and urochloa images moved into their folders.")
