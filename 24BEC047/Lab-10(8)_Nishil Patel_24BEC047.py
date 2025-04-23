def q8():
    f_r = open('8_in.txt', 'r')
    data = f_r.read()
    f_r.close()

    print("Original Text:", data)

    remove_words = [
        ' a ', ' an ', ' the ', ' A ', ' An ', ' The ',  # word surrounded by spaces
        'a ', 'an ', 'the ', 'A ', 'An ', 'The ',       # word at start
        ' a', ' an', ' the', ' A', ' An', ' The'        # word at end
    ]
    for word in remove_words:
        data = data.replace(word, ' ')  

    
    fw = open('8_out.txt', 'w')
    fw.write(data)
    fw.close()

    print("Modified Text Written to 8b.txt")

q8()
