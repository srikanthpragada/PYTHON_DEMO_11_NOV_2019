class A:
    pass
    # def fun(self):
    #     print("A")


class B:
    def fun(self):
        print("B")


class C(A, B):
    pass
    # def fun(self):
    #     print("C")


obj = C()
obj.fun()
print(C.mro())
