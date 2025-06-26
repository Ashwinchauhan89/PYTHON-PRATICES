class Parent1():
    def parent1(self):
        print("Parent1 method called")

class Parent2():
    def parent2(self):
        print("Parent2 method called")

class Child(Parent1, Parent2):
    def child(self):
        print("Child method called")

obj = Child()
obj.parent1()
obj.parent2()
obj.child()