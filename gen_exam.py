import random
import time
import memory_profiler

names=['preeti','viaan','diya','aarav']
major=['eng','hindi','maths','science']

print 'Memory Before is {}Mb'.format(memory_profiler.memory_usage())

def person_List(nums_people):
    result=[]
    for i in xrange(nums_people):
        Person={
                    'id':i,
                    'names':random.choice(names),
                    'major':random.choice(major)
                    
               }
        result.append(Person)
    return result

def person_Gen(nums_people):
    for i in xrange(nums_people):
        Person={
                    'id':i,
                    'names':random.choice(names),
                    'major':random.choice(major)
                    
               }
        yield Person
t1=time.clock()
print(person_List(100ççç))
#print (person_Gen(5))
t2=time.clock()



print 'Memory After is {}Mb'.format(memory_profiler.memory_usage())
print 'Took {} seconds' .format(t2-t1)
