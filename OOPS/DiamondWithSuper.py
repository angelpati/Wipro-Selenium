class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        super().show()
class C(A):
    def show(self):
        print("C")

class D(B,C):
    def show(self):
        super().show()
        print("D")
d=D()
d.show()
print(D.mro())