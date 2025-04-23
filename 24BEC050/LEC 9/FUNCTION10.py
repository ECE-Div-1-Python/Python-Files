def frequency(n):
    l=n.lower().split()

    word={}
    for words in l:
        words.join(char for char in words if char.isalnum())
        if words:
            word[words]=word.get(words,0)+1
    return word
text="this is a text , this test is only a test"
print(frequency(text))

