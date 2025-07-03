class Parent():
    def parent(self):
        print("this is my parent class")


class Intermediate1(Parent):
    def intermediate1(self):
        print("THis is my Intermediate 1 class")

class Intermediate2(Parent):
    def intermediate2(self):
        print("This is intermediate 2 class")

class Child(Intermediate1,Intermediate2):
    def child(self):
        print("This is my Child class")

obj=Child()


obj.child()
obj.intermediate1()
obj.intermediate2()
obj.parent()

