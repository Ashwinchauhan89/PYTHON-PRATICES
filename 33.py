class Overloading():
    def show(self):
        print("This is my show method")

    def show(self, First=""):
        print("This is my show method with one argument", First)

    def show(self, First="", Second=""):
        print("This is my show method with two arguments", First, Second)
obj=Overloading()
obj.show()  
obj.show("Hello")
obj.show("Hello", "World")

class Over():
    def __init__(self, *args):
        print(args)
obj=Over(10)
obj=Over(1, 2, 3)
obj=Over(1,2,34,5)  # This will print the tuple (