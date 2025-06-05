#using constructors
class Baby:
    nam=""
    rollno=0
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def myfun(self,name):
        print(f"hello {name}")
s=Baby("baby",42)
print(s.name,s.rollno)
s.myfun("baby")