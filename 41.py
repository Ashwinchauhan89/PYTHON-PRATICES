class Parent():
    def parent(self):
        print("parent method is called")

class Child(Parent):
    def child(self):
        print("Child method is called")

obj=Child()
obj.child()
obj.parent()