
source_file = "input.txt"
destination_file = "output.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line.upper())

print("File copied with content converted to uppercase into another.")
