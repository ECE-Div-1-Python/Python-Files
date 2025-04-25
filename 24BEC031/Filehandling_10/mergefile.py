def merge(f1, f2, output_file):
    try:

        with open(f1, 'r') as f1, open(f2, 'r') as f2:
            l1 = f1.readlines()
            l2 = f2.readlines()

        with open(output_file, 'w') as out_file:

            max_ln = max(len(l1), len(l2))

            for i in range(max_ln):
                if i < len(l1):
                    out_file.write(l1[i])
                if i < len(l2):
                    out_file.write(l2[i])

        print(f"Merged content written to '{output_file}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

file1 = 'files/file1.txt'
file2 = 'files/file2.txt'
output_file = 'files/merged_output.txt'

merge(file1, file2, output_file)
