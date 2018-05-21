    
N = int(raw_input("Enter number of commands"))
l=[]

for i in range(N):
    usr_input=raw_input("Enter the command")
    #print usr_input
    usr_input_list=usr_input.split(" ")
    cmd=usr_input_list[0]
    args=usr_input_list[1:]
    cmd_new=cmd+"("+ ",".join(args)+")"
    #print cmd_new
    if cmd!="print":
        eval("l."+cmd_new)
    else:
        print l

