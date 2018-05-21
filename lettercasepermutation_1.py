def letterCasePermutation(S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
                print res
            else:
                res = [i+ch for i in res]
                print res
        return res

print(letterCasePermutation("a12b"))
