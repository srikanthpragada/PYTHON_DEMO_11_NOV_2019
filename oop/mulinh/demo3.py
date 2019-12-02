class A:
    def fun(self):
        print("A")


class B(A):
    pass
    # def fun(self):
    #     print("B")


class C(A):
    def fun(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.fun()
print(D.mro())
