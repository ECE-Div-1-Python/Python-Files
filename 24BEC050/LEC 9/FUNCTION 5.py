import string
def is_pangram(s):
    s_sub=set(string.ascii_lowercase)
    s=set(s.lower())
    return s <= s_sub
a="The quick brown fox jumps over the lazy dog"
print(is_pangram(a))
b="Crazy Fredrick bought many very exquisite opal jewels"
print(is_pangram(b))


