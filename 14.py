class Parent1():
    def parent1(self):
        print("ths is my parent 1")


class Parent2():
    def parent2(self):
        print("this is my  parent 2")

class Child(Parent1,Parent2):
    def child(self):
        print("this is child class")


obj=Child()
obj.child()
obj.parent1()
obj.parent2()
