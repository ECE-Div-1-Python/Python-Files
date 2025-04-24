print("Name: Rutva Mehta")
print("Rollno.: 24BEE122")

# Define file names
input_file = "input.txt"
output_file = "cleaned_text.txt"

# Open the input file and read lines
with open(input_file, "r") as file:
    lines = file.readlines()

# List of words to remove
remove_words = ["a", "an", "the"]

# Process each line
with open(output_file, "w") as file:
    for line in lines:
        words = line.split()  # Split line into words
        new_words = [word for word in words if word.lower() not in remove_words]  # Remove unwanted words
        file.write(" ".join(new_words) + "\n")  # Write cleaned line

print(f"File '{output_file}' created successfully with words removed.")
