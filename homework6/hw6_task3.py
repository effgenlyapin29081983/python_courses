class Worker:

    def __init__(self, thname, thsurname, thposition, thwage, thbonus):
        self.name = thname
        self.surname = thsurname
        self.position = thposition
        self.income = {}
        self.income.update({"wage": thwage})
        self.income.update({"bonus": thbonus})


class Position(Worker):
    def get_fullname(self):
        fullname = self.name + " " + self.surname
        print("Full name: ", fullname)

    def get_total_income(self):
        print("Total income = ", self.income.get("wage") + self.income.get("bonus"))


fposition = Position("Ivan", "Ivanov", "Pos1", 35, 45)
sposition = Position("Peter", "Petrov", "Pos2", 45, 55)
tposition = Position("Sidor", "Sidorov", "Pos3", 55, 65)

fposition.get_fullname()
fposition.get_total_income()

sposition.get_fullname()
sposition.get_total_income()

tposition.get_fullname()
tposition.get_total_income()