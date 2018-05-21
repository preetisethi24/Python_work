def question8():
    input_words=raw_input("Enter words:")
    words=[words for words in input_words.split(",")]
    words.sort()
    print ','.join(words)

question8()
