import os
import shutil
def fcopy():
    # Define the source and destination directories and the file to copy
    source = 'files'
    dest = 'new_files'
    filename = 'files/imbadatnamingstuff.txt'

    if not os.path.exists(source):
        os.mkdir(source)
        print(f"Created source directory: {source}")

    if not os.path.exists(dest):
        os.mkdir(dest)
        print(f"Created destination directory: {dest}")

    source_file = os.path.join(source, filename)
    dest_file = os.path.join(dest, filename)

    if not os.path.exists(source_file):
        with open(source_file, 'w') as f:
            f.write("MIIIIIIAAAUUUUUU :3")
        print(f"file fAbRiCAtEd at {source_file}")

    try:
        shutil.copy(source_file, dest_file)
        print(f"File '{filename}' copied successfully from {source} to {dest}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in {source}.")

fcopy()
