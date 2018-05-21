def reverse_string1(s):
    return s[::1]

import timeit
s ='abdjsfjkfdkfjff'*10
print(timeit.repeat(lambda:reverse_string1(s)))


