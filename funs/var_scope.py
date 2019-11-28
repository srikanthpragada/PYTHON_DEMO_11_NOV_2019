a = 10

def fun():
    global a
    a = a + 1
    b = 20
    def lfun():
        nonlocal b   # ref to enclosing variable
        c = 30
        b = b +  1
        print(b)

    lfun()
    print(b)
    print(a)


fun()
print(a)

