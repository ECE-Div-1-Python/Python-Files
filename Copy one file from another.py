import os

source_file = "source_folder/example.txt"
destination_dir = "destination_folder/new_subdir"
destination_file = os.path.join(destination_dir, "example.txt")

os.makedirs(destination_dir, exist_ok=True)

with open(source_file, "rb") as src:
    content = src.read()

with open(destination_file, "wb") as dst:
    dst.write(content)

print(f"Copied '{source_file}' to '{destination_file}' successfully.")

