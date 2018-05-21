import itertools
def letterCasePermutation(S):
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        for i in itertools.product(*L):
        return "".join(i)

letterCasePermutation("a34b")
