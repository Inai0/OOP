class SSS:
    def __init__(self, int):
        self.int = int+2

class S(SSS):
    def __init__(self,integer):
        self.INT=integer-1

class SS(SSS):
    def __init__(self, int):
        self.int=int+10
        print (self.int)
        super().__init__(int)
        print (self.int)
        self.acces=S(int)
    
    
ob1=SSS(12)
ob2 = SS(15)
print (ob2.acces.INT)
print (isinstance(ob1, SSS))
print (issubclass(SS, SSS))