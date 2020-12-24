from abc import ABC, abstractmethod

class Clothes(ABC):
    all_quantity = 0
    @abstractmethod
    def quantity(self):
        pass

class Coat(Clothes):
    @property
    def quantity(self):
        self.size = int(input("Enter size:\n"))
        self.quant = self.size/6.5 + 0.5
        self.all_quantity += self.quant
        return self.quant

class Costume(Clothes):
    @property
    def quantity(self):
        self.growth = int(input("Enter growth:\n"))
        self.quant =  self.growth*2 - 0.3
        self.all_quantity += self.quant
        return self.quant

a = Coat()
a.quantity
b = Costume()
b.quantity
c = Costume()
print(f"Final quantity = {c.quantity}")

