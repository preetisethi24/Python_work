def set_discard():
    n = int(raw_input("enter no of elements:"))
    s = set(map(int,raw_input("enter elements").split()))
    no_cmd = int(raw_input("enter no of command"))
    for i in range(no_cmd):
        s.raw_input("enter command")()

set_discard()
