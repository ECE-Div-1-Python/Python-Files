def merge_files_alternately(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            if i < len(lines1):
                out.write(lines1[i])
            if i < len(lines2):
                out.write(lines2[i])

    print(f"Merged content written to {output_file} ")


merge_files_alternately('files/file6_1.txt', 'files/file6_2.txt', 'files/file6_out.txt')

