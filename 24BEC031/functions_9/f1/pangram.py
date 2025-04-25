import string
def ispangram(s):
    # initialize set of lowercase alphabets
    alpset = set(string.ascii_lowercase)
    input_set = set(s.lower())
    # Remove non alphabets
    input_set = {char for char in input_set if char in alpset}

    #check for alphabets
    if input_set >= alpset:
        return True
    else:
        return False

ts1 = "Sphinx of black quartz, judge my vow"
if ispangram(ts1):
    print("The given string is a pangram.")
else:
    print("The given string is not a pangram.")

