class A:
    def fun1(self):
        print("Hello Woorld!")
class B(A):
    def fun2(self):
        print("<===Hello people===>")
class C(B):
    def fun3(self):
        print("How aer you guys!")
x=C()
x.fun1()
x.fun2()
x.fun3()


# using hierarchical Inheritance
class D:
    pass 
    def func1(self):
        print("HELLOO GUYS")
class E(D):
    pass 
    def func2(self):
        print("HAI") 
x=E()
x.func2()
class F(D):
    pass 
    def func3(self):
        print("ok Bye Thank you")
f=F()
f.func1()
f.func3()



# using hybrid inheritance
class A:
    def spek(self):
        print("bow bow")
class B(A):
    def spek1(self):
        print("meow meow")
class C:
    def spek2(self):
        print("C")
class D(B,C):
    def spek3(self):
        print("D")
b=D()
b.spek()
b.spek1()
b.spek2()
b.spek3()