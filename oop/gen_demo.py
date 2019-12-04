
def numbers():
    for i in range(1,11):
        yield i


g = numbers()

for n in g:
    print(n,end = ' ')
