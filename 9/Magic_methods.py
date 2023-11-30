class SSS:
    def __init__(self, name, integer):
        self.integer = integer
        self.name = name

    def __str__(self):
        return f"Class name: {self.name}"

    def __add__(self, other):
        return self.integer + other.integer

class SS(SSS):
    def __init__(self, name, integer):
        self.integer=integer
        self.name = "NAME"

ob1 = SSS("name", 10)
ob2 = SS("", 5)
print(ob1)
print(ob2)
print(ob1 + ob2)
