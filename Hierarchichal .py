class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class c(A):
    def display_C(self):
        print("from class-c")
s=B()
P=c()
s.display_A()
s.display_B()
P.display_C()