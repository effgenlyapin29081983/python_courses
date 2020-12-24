class Cell():
    def __init__(self, *args):
        if len(args) == 0:
            self.size = int(input("Enter size cell:\n"))
        else:
            if args[0] > 0:
                self.size = args[0]
            else:
                self.size = 0
                print("Size can't negative or equal 0")

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self.size > other.size:
            return Cell(self.size - other.size)
        else:
            print("Size can't negative!!!")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(int(self.size/other.size))

    def make_order(self):
        if self.size > 0:
            self.order = int(input("Enter size string:\n"))
            self.cel = int(self.size // self.order)
            self.drob = int(self.size % self.order)

            for el in range(0, self.cel):
                print('*'*self.order + '\n')
            if self.drob>0:
                print('*'*self.drob)
        else:
            pass


a = Cell()
a.make_order()
b = Cell()
b.make_order()

#c = a + b
#c.make_order()

#d = a - b
#d.make_order()

#e = b - a
#e.make_order()

#f = a * b
#f.make_order()

g = a / b
g.make_order()

