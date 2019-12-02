class A:
    def fun(self):
        print("A")


class B(A):
    def fun(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.fun()
