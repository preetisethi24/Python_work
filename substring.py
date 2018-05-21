##def count_substring(string, sub_string):
##    if sub_string in string:
##        index=string.index(sub_string)
##        return index
##    else:
##        return -1
##
##
##print(count_substring("ABCDCDC","CD"))

def count_substring(string, sub_string):
    count = 0
    print len(string)
    print len(sub_string)
    for i in range(len(string)-len(sub_string)+1):
        print(string[i:i+len(sub_string)])
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count

print(count_substring("ABCDCDC","CD"))
