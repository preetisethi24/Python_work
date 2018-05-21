def find_anagram():
    loc="/Users/preetisethi/anagram.txt"
    with open(loc) as f:
        h=f.read()
        print type(h)
        l=h.split('\n')
        print l
        print h
        print type(h)
    f.close()

find_anagram()
