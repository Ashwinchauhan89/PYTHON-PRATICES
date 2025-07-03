class Encapulsation():
    __sno = 0
    __sname = ""

    def setSno(self, sno):
        self.__sno = sno    

    def setSname(self, sname):
        self.__sname = sname
    
    def getSno(self):
        return self.__sno

    def getSname(self): 
        return self.__sname
obj = Encapulsation()
obj.setSno(101) 
obj.setSname("Ashwin")
print(obj.getSno())
print(obj.getSname())
# This code demonstrates encapsulation in Python by using private attributes and public methods to set and get their values.


