def remwords(inp_f, out_f):
    try:

        with open(inp_f, 'r') as infile:
            content = infile.read()

        rem_words = ['MEEU','miu','rat']


        for word in rem_words:

            content = content.replace(f" {word} ", " ")
            content = content.replace(f" {word}.", " .")
            content = content.replace(f" {word},", " ,")

        with open(out_f, 'w') as outfile:
            outfile.write(content)

        print(f"Content written to '{out_f}' with specified words removed.")

    except FileNotFoundError:
        print(f"Error: The file '{inp_f}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

infile = 'files/file1.txt'
out_file = 'files/f3.txt'

remwords(infile, out_file)
