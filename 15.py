class Parent():
    def parent(self):
        print("This is my Parent class")

class Child1(Parent):
    def child1(self):
        print("This is my child 1 class ")

class Child2(Parent):
    def child2(self):
        print("This is my child 2 class")

obj=Child1()
obj.child1()
obj.parent()

obj=Child2()
obj.child2()
obj.parent()