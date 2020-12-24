class NullSize(Exception):
    def __init__(self, text):
        self.txt = text


class Matrix:

    def __init__(self, *args):
        if len(args) == 0:
            self.inputMatrix()
        else:
            size_eq = True
            for i in range(1, len(args[2])):
                if len(args[2][i]) != len(args[2][i-1]):
                    size_eq = False
                    break
            if size_eq:
                self.arr_Matrix = []
                #print("SIZE EQ")
                self.weight = args[0]
                self.height = args[1]
                #print(len(args))
                #for el in args:
                for el in args[2]:
                    self.arr_Matrix.append(el)
                #print(f"W={self.weight}, H={self.height}")

    def inputMatrix(self):
        self.weight = int(input("Enter weight matrix:\n"))
        self.height = int(input("Enter height matrix:\n"))
        self.arr_Matrix = []
        try:
            if self.weight <= 0 or self.height <= 0:
                raise NullSize("Size of Matrix <=0!!!")
        except NullSize as ns:
            print(ns)
        else:
            try:
                for els in range(0, self.height):
                    inp_str = input(f"Enter {els} string:\n").split()
                    if len(inp_str) == self.weight:
                        self.arr_Matrix.append([int(el) for el in inp_str])
                        #print(self.arr_Matrix[els])
                    else:
                        raise NullSize("Size input string <> size string Matrix")
            except NullSize as ns:
                print(ns)

    def __str__(self):
        print("Output Matrix:")
        out = ""
        for el in self.arr_Matrix:
            out += " ".join(map(str, el))+'\n'
        return out

    def __add__(self, other):
        try:
            if self.weight == other.weight and self.height == other.height:
                res_m = []
                for i in range(0, self.height):
                    res_str = []
                    for j in range (0, self.weight):
                        res_str.append(self.arr_Matrix[i][j] + other.arr_Matrix[i][j])
                    res_m.append(res_str)
                #print(res_m)
                return Matrix(self.weight,self.height,res_m)
            else:
                raise NullSize("Different sizes!!!")
        except NullSize as ns:
            print(ns)
            return Matrix(0,0,[])

a = Matrix()
print(a)
b = Matrix()
print(b)
c = a+b
print(c)
