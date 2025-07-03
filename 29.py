class Default():
    def defult(self):
        print("The default constructoe are used")
obj=Default()
obj.defult()

class Peramiterized():
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj=Peramiterized("ashwin","30")
print(obj.name)
print(obj.age)

