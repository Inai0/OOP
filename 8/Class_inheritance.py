class SSS:
    def __init__(self, int):
        self.int = int+2

    def class_name(self):
        pass

class A(SSS):
    def class_name(self):
        
        return "A"

class S(SSS):
    def class_name(self):
        return "S"

class SS(SSS):
    def __init__(self, int):
        self.int=int+10
        print (self.int)
        super().__init__(int)
        print (self.int)
    def class_name(self):
        return "SS"
    
ob1=SSS(12)
ob2 = SS(15)
