def question13(sentence):
    digits=[]
    letters=[]
    for s in sentence:
        if s.isdigit():
            digits.append(s)
        elif s.isalpha():
            letters.append(s)
        else:
            pass
    print "DIGITS", len(digits)
    print "LETTERS", len(letters)
     
question13("hello world! 123")
