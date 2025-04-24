s=("anuj","anupama","arpit","bobzy","bagha")
print(s)
sa=set()
sb=set()
for nm in s:
    if nm[0]=="a":
        sa.add(nm)
    elif nm[0]=='b':
        sb.add(nm)
print(sa)
print(sb)        
