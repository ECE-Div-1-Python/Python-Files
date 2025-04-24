def frequency(s):
    c=0
    d={}
    l=s.split()
    for i in l:
        c=s.count(i)
        d[i]=c
    print(d)
frequency('cat is is mat')