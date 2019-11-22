def greet(*names, msg="Hello"):
    # print(type(names))
    for n in names:
        print(msg, n)


greet("Bill", "Steve", msg="Hi")
greet("Tom", "Larry", "Elon")


