def fun():
    print("fun?")
def disp():
    print("displaey")
def msg():
    print("mesej")

funcs = [fun, disp, msg]
for f in funcs:
    f()
