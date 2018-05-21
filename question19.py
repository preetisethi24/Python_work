from operator import itemgetter, attrgetter

l = []
while True:
    s = raw_input("Enter name,age,height:")
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=attrgetter('age'))
