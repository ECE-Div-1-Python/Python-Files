

def merge_files_alternatively(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
     
        len1, len2 = len(lines1), len(lines2)
        
       
        for i in range(max(len1, len2)):
            if i < len1:
                out.write(lines1[i])
            if i < len2:
                out.write(lines2[i])

merge_files_alternatively('file1.txt', 'file2.txt', 'merged_output.txt')
