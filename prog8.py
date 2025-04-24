


input_file = "input.txt"
output_file = "cleaned_text.txt"


with open(input_file, "r") as file:
    lines = file.readlines()


remove_words = ["a", "an", "the"]

with open(output_file, "w") as file:
    for line in lines:
        words = line.split()  # Split line into words
        new_words = [word for word in words if word.lower() not in remove_words]  # Remove unwanted words
        file.write(" ".join(new_words) + "\n")  # Write cleaned line

print(f"File '{output_file}' created successfully with words removed.")
