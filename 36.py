class Add():
    def add(self,a,b):
        return a+b
    

class Subtarction():
    def sub(self,a,b):
        return a-b
    

class Multiplication():
    def mul(self,a,b):
        return a*b
    
class Division():
    def div(self,a,b):
        return a/b
    
class Calculator(Add,Subtarction,Multiplication,Division):
    pass

obj=Calculator()
a=float(input("Enter the First Number"))
b=float(input("Enter the second Nummber"))


print(obj.add(a,b))
print(obj.sub(a,b))
print(obj.mul(a,b))
print(obj.div(a,b))
    
