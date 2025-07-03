class Grandparent():
    def grandparent(self):
        print("this is my grand parent class")

class Parent(Grandparent):
    def parent(self):
        print("This is my parent class")

class Child(Parent):
    def child(self):
        print("This is child class")

obj=Child()

obj.grandparent()
obj.parent()
obj.child()



