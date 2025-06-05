class Sample:
    def spa(self):
        print("hai")
class Baby:
    def span(self):
        print("hello")
class Jaya(Sample,Baby):
    def spanl(self):
        print("how are you")
x=Jaya()
x.spa()
x.span()
x.spanl()