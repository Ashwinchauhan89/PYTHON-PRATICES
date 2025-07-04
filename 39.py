class Parent1():
    def parent1(self):
        print("parent 1 method is called")


class Parent2():
    def parent2(self):
        print("parent 2 method is called")

class Child(Parent1,Parent2):
    def child(self):
        print("child method is called")

obj=Child()

obj.child()
obj.parent1()
obj.parent2()