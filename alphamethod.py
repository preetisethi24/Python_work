def alphamethod(s):
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.upper() for c in s))
        
        
alphamethod("ADB!")
