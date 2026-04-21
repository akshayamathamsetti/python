class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class c(A):
    def display_C(self):
        print("from class-c")
class D(B,c):
    def display_D(self):
        print("from class D")
s=D()
s.display_A()
s.display_B()
s.display_C()