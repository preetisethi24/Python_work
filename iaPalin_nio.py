class isPalindrome:
    def is_palin(self,word):
        first=word[0]
        last=word[-1]
        middle=word[1:-1]
        if len(word)<=1:
            return True	
        elif first!=last:
            return False
        else:
            return is_palin(middle)
    
x=isPalindrome()
print(x.is_palin("mom"))
