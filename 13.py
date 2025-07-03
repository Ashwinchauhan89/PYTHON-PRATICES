class Parent():
    def parent(self):
        print("This is my parent class")


class Child(Parent):
    def child(self):
        print("This is child class")

obj=Child()
obj.child()
obj.parent()