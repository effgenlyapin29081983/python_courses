class Stationery:
    def __init__(self,th_name):
        self.name = th_name
        print(f"Create object with name = {self.name}")
    def draw(self):
        print("start draw!!!")


class Pen(Stationery):
    def draw(self):
        print("draw pen!!!")


class Pencil(Stationery):
    def draw(self):
        print("draw pencil")


class Marker(Stationery):
    def draw(self):
        print("draw marker")


brush = Stationery("brush")
brush.draw()

pen = Pen("pen")
pen.draw()

pencil = Pencil("pencil")
pencil.draw()

marker = Marker("marker")
marker.draw()