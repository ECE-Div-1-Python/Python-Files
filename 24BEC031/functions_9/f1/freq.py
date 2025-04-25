def frequency(s):
    ws = s.split()
    wc = {}
    #Count the frequency of each word
    for w in ws:
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1

    #sort
    Swc = dict(sorted(wc.items()))
    return Swc

usrst = "miau mau miau mau meow miau miu meow awiwiwi"
f = frequency(usrst)

print(f"Word frequencies (sorted): {f}")
