# using  inheritance
class Dog():
    pass
    def myfun(self):
        print(" The dog is barking")
class Cat(Dog):
    pass 
    def  myfun1(self):
        print("cat  is barking")
s=Cat()
s.myfun()
s.myfun1()



# usig single inheritance
class Human:
    eye=2
    hands=2
    def eat(self):
        print("I am  eating")
class Female(Human):
    gender="female"
    def gree(self,name):
        print("hai " )
x=Female()
print(x.eye)
Human.eat("")
print(x.gender)
x.gree("")

