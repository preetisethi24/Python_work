import timeit
import random

#def random_sort(n):
#   return sorted([random.random() for i in range(n)])

#Timer(random_sort(2000000)).timeit()

timeit.timeit('"-".join(str(n) for n in range(100))', number=10)
