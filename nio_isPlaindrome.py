class checkPalindrome:
    def isPalindrome(self,word):
        for i in xrange(len(word)/2):
            if word[i]!=word[len(word)-i-1]:
                print"Word is NOT a Plaindrome"
                break
        else:
            print"Word is a Plaindrome"


x=checkPalindrome()
x.isPalindrome("helloolleh")
            
