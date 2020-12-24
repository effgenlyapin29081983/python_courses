class Sklad:
    def __init__(self):
        self.items = {}
        self.transactions = {}
        self.itemNum = 0
        self.transNum = 0
    def addItem(self, item):
        add_item = False
        for its in range(1, len(self.items)+1):
            th_Item = self.items.get(its)
            if th_Item.characteristics.get('name') == item.characteristics.get('name') and th_Item.characteristics.get('model') == item.characteristics.get('model'):
                th_Item.characteristics.update({'count': th_Item.characteristics.get('count')+item.characteristics.get('count')})
                add_item = True
                print("find item and add!!!")
                self.transNum += 1
                self.transactions.update({self.transNum: f"in {its} adding {item.characteristics.get('count')} items"})
        if not add_item:
            self.itemNum += 1
            self.items.update({self.itemNum: item})
            print("add new item!!!")
            self.transNum += 1
            self.transactions.update({self.transNum: f"new item {self.itemNum} adding {item.characteristics.get('count')} items"})

    def sendItem(self, item, toDep):
        send_item = False
        for its in range(1, len(self.items)+1):
            th_Item = self.items.get(its)
            if th_Item.characteristics.get('name') == item.characteristics.get('name') and th_Item.characteristics.get('model') == item.characteristics.get('model') and th_Item.characteristics.get('count') >= item.characteristics.get('count'):
                th_Item.characteristics.update({'count': th_Item.characteristics.get('count') - item.characteristics.get('count')})
                send_item = True
                print("find item and send!!!")
                self.transNum += 1
                self.transactions.update({self.transNum: f"in {its} send {item.characteristics.get('count')} to {toDep}"})
        if not send_item:
            print("can't send this count item")

    def printItems(self):
        if len(self.items) > 0:
            print("Items in Sklad:")
            for its in range(1, len(self.items) + 1):
                th_Item = self.items.get(its)
                print(th_Item.characteristics)

    def printTransactions(self):
        if len(self.transactions) > 0:
            print("Transactions in Sklad:")
            for its in range(1, len(self.transactions) + 1):
                print(self.transactions.get(its))


class Technic:
    def __init__(self, * args):
        self.characteristics = {}
        if len(args) == 0:
            self.characteristics.update({'name': input("Enter name of technic:\n")})
            self.characteristics.update({'model': input("Enter model of technic:\n")})
            self.characteristics.update({'count': int(input("Enter count of technic:\n"))})
            self.characteristics.update({'buy_price': float(input("Enter buy price of technic:\n"))})
            self.characteristics.update({'sell_price': float(input("Enter sell price of technic:\n"))})
        else:
            self.characteristics.update({'name': args[0]})
            self.characteristics.update({'model': args[1]})
            self.characteristics.update({'count': int(args[2])})
            self.characteristics.update({'buy_price': float(args[3])})
            self.characteristics.update({'sell_price': float(args[4])})


class Printer(Technic):
    def __init__(self, * args):
        super().__init__(* args)
        if len(args) == 0:
            self.characteristics.update({'format_paper': input("Enter format paper of technic:\n")})
            self.characteristics.update({'nom_voltage': int(input("Enter nominal voltage of technic:\n"))})
            self.characteristics.update({'type': input("Enter type technic (laser,matrix,ink):\n")})
        else:
            self.characteristics.update({'format_paper': args[5]})
            self.characteristics.update({'nom_voltage': int(args[6])})
            self.characteristics.update({'type': args[7]})


class Copier(Technic):
    def __init__(self, * args):
        super().__init__(* args)
        if len(args) == 0:
            self.characteristics.update({'format_paper': input("Enter format paper of technic:\n")})
            self.characteristics.update({'nom_voltage': int(input("Enter nominal voltage of technic:\n"))})

        else:
            self.characteristics.update({'format_paper': args[5]})
            self.characteristics.update({'nom_voltage': int(args[6])})


class Scanner(Technic):
    def __init__(self, *args):
        super().__init__(*args)
        if len(args) == 0:
            self.characteristics.update({'format_paper': input("Enter format paper of technic:\n")})
            self.characteristics.update({'nom_voltage': int(input("Enter nominal voltage of technic:\n"))})

        else:
            self.characteristics.update({'format_paper': args[5]})
            self.characteristics.update({'nom_voltage': int(args[6])})


mySklad = Sklad()
#a = Printer()
#print(a.characteristics)
#mySklad.addItem(a)
b = Printer("Riccoh", "123", "3", "32.5", "45.8", "A2", "210", "laser")
print(b.characteristics)
mySklad.addItem(b)
#c = Copier()
#print(c.characteristics)
#mySklad.addItem(c)
d = Copier("Xerox", "123", "3", "32.6", "45.9", "A4", "210")
print(d.characteristics)
mySklad.addItem(d)
#e = Scanner()
#print(e.characteristics)
#mySklad.addItem(e)
f = Scanner("HP", "123", "3", "32.4", "45.6", "A4", "210")
print(f.characteristics)
mySklad.addItem(f)
mySklad.printItems()
mySklad.printTransactions()
a = Printer("Riccoh", "123", "3", "32.5", "45.8", "A2", "210", "laser")
print(a.characteristics)
mySklad.addItem(a)
mySklad.printItems()
mySklad.printTransactions()
c = Scanner("HP", "123", "2", "32.4", "45.6", "A4", "210")
print(c.characteristics)
mySklad.sendItem(c,"ASU")
mySklad.printItems()
mySklad.printTransactions()
e = Copier("Xerox", "123", "5", "32.6", "45.9", "A4", "210")
print(e.characteristics)
mySklad.sendItem(e,"ASU")
mySklad.printItems()
mySklad.printTransactions()
