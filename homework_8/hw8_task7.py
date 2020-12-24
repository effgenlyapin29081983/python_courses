class MyComplex():
    def __init__(self,* args):
        if len(args)==0:
            self.Re = float(input("Enter Re():\n"))
            self.Im = float(input("Enter Im():\n"))
        else:
            self.Re = args[0]
            self.Im = args[1]

    def __add__(self, other):
        return MyComplex(self.Re+other.Re,self.Im+other.Im)

    def __mul__(self, other):
        return MyComplex(self.Re*other.Re-self.Im*other.Im,self.Im*other.Re+self.Re*other.Im)

    def __str__(self):
        return f"{self.Re}+{self.Im}i"

a = MyComplex()
b = MyComplex()
c = a + b
print(c)
d = a * b
print(d)
