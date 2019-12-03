class A:
    def __init__(self):
        print(type(self))
        print("A")

obj_a = A()

class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


obj = C()
