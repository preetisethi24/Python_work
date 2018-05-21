l=[]
for _ in range(int(raw_input("Enter the value os N:"))):
    name = raw_input("Enter the name:")
    score = float(raw_input("Enter the Score:"))
    print name,score
    l.append([name,score])
print l
new_list=sorted(set([score for name,score in l]))[1]
print new_list

print "\n".join([a for a,b in sorted(l) if b==new_list])
