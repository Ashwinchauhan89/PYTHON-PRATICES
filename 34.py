class Main():
    def sound(self):
        print("sound of animal")

class Dog(Main):
    def sound(self):
        print("barking")

obj=Dog()
obj.sound()  # This will call the sound method from the Dog class
obj=Main()
obj.sound()  # This will call the sound method from the Main class