def copi(source, dest):
    try:
        with open(source, 'r') as source:
            cont = source.read()

        content_upper = cont.upper()

        with open(dest, 'w') as destination:
            destination.write(content_upper)

        print(f"Contents copied from '{source}' to '{dest}' with all characters converted to uppercase.")

    except FileNotFoundError:
        print(f"Error: The file '{source}' was not found.")



source_file = ('files/mau.txt')
dest_file = ('files/MAEU.txt')

copi(source_file, dest_file)
