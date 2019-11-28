def zero(n):
    print(id(n))
    n = 0
    print(id(n))


a = 100
print(id(a))
zero(a)
print(a)


def prepend(l, n):
    l.insert(0, n)


lst = [1, 2, 3]
prepend(lst, 10)
print(lst)
