class SSS:

    def __init__(self,name):
        self.name=name

class SS(SSS):

    def __init__(self,name):
        self.name="NAME"

ob1 = SSS("name")
ob2 = SS("")
print (ob1.name)
print (ob2.name)