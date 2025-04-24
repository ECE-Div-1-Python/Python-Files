import string 
def ispangram(sentence):
    
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    
    return alphabet_set <= sentence_set

test_sentence1 = "The quick brown fox jumps over the lazy dog"
test_sentence2 = "Crazy Fredrick bought many very exquisite opal jewels"
test_sentence3 = "This is not a pangram sentence"

print(f"Is pangram? '{test_sentence1}' -> {ispangram(test_sentence1)}")
print(f"Is pangram? '{test_sentence2}' -> {ispangram(test_sentence2)}")
print(f"Is pangram? '{test_sentence3}' -> {ispangram(test_sentence3)}")
