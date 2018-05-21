def question17():
    netAmount=0
    while True:
        s=raw_input("enter the number:")
        if not s:
            break
        values=s.split(" ")
        operation=values[0]
        amount=int(values[1])
        if operation=="D":
            netAmount+=amount
        else:
            netAmount-=amount
    print netAmount

question17()
