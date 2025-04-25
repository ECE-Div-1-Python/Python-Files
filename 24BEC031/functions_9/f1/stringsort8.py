# func to convert
def convert(s):
    w = s.split()
    # Remove dupliketes
    uw = set(w)

    # alphabetical sorting
    sw = sorted(uw)
    return ' '.join(sw)

S = "miao mao miao mao lala lala la"
print(f"Converted string: {convert(S)}")
