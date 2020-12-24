import time

class TrafficLight():
    def __init__(self):
        pass

    __colour = {"red": "\033[31m {}", "yellow": "\033[33m {}", "green": "\033[32m {}"}
    __timers = {"red": 7, "yellow": 2, "green": 10}
    trend = "+"
    this_colour="red"



    def out(self, col, col_val):
        print(col_val.format(col))
    def check(self,col,next_col):
        if ((col=="red" or col=="green") and next_col!="yellow") or (col=="yellow" and ((self.trend=="+" and next_col!="green") or (self.trend=="-" and next_col!="red"))):
            exit()
        else:
            return self.__colour.get(next_col)

    def running(self):
        self.out(self.this_colour,self.__colour.get(self.this_colour))
        time.sleep(self.__timers.get(self.this_colour))
        while True:
            if self.this_colour == "red":
                self.trend="+"
            elif self.this_colour == "green":
                self.trend="-"
            else:
                pass
            next_colour = input("Enter next colour:\n")
            self.out(next_colour,self.check(self.this_colour, next_colour))
            time.sleep(self.__timers.get(next_colour))
            self.this_colour=next_colour

svetofor = TrafficLight()
svetofor.running()