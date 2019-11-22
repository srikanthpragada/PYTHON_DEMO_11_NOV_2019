def process():
    print("Processing")


task = process
print(id(process))
print(id(task))


def process(msg):
    print("Processing again with msg = ", msg)


print(id(process))
