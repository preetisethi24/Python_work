class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)==len(B) and B in A+A:
            return True
        else:
            return False
        
s=Solution()
print(s.rotateString('abcde','cdeab'))
