a=['a','and','the']

with open("files/file 8.txt",'r') as f:
    with open("files/file 8o.txt",'w') as g:
        for line in f:
            fil=" ".join(w for w in line.split() if w not in a )
            g.write(fil)

print("your file is completely changed!")
