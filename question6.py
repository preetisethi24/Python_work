import math
c=50
h=30
values=[]
input_str=raw_input("Enter the values:")
input=[x for x in input_str.split(',')]
print input
for d in input:
    values.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(values)
        
