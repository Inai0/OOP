def Funk(a,b,c):
    return a,b,c
print (Funk(1,'a',True))
def Funk2(a,b):
    print (a+b())
def Funk3():
    return 10
Funk2(5,Funk3)