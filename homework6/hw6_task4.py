class Car:
    def __init__(self, th_name, th_color, th_speed, th_is_police):
        self.name = th_name
        self.color = th_color
        self.speed = th_speed
        self.is_police = th_is_police

    def show_speed(self):
        print(f"Speed({self.name}) = {self.speed}")

    def go(self):
        print(f"Car {self.name} go!!!")

    def stop(self):
        print(f"Car {self.name} stop!!!")

    def get_color(self):
        print(f"Color ({self.name}) is {self.color}")

    def get_is_police(self):
        print(f"{self.name} is police") if self.is_police else print(f"{self.name} is not police")

    def turn(self, direction):
        print(f"Car ({self.name}) go {direction}")


class TownCar(Car):
    def __init__(self, th_name, th_color, th_speed):
        self.name = th_name
        self.color = th_color
        self.speed = int(th_speed)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"Speed car({self.name}) > 60")
        else:
            print(f"Speed({self.name}) = {self.speed}")


class WorkCar(Car):
    def __init__(self, th_name, th_color, th_speed):
        self.name = th_name
        self.color = th_color
        self.speed = int(th_speed)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"Speed car({self.name}) > 40")
        else:
            print(f"Speed({self.name}) = {self.speed}")


class SportCar(Car):
    def __init__(self, th_name, th_color):
        self.name = th_name
        self.color = th_color
        self.speed = 300
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, th_name, th_color, th_speed):
        self.name = th_name
        self.color = th_color
        self.speed = int(th_speed)
        self.is_police = True


car = Car("Moskvich", "green", 140, False)
car.get_color()
car.go()
car.stop()
car.get_is_police()
car.show_speed()
car.turn("left")

workCar1 = WorkCar("GAZ", "blue", 60)
workCar1.get_color()
workCar1.go()
workCar1.stop()
workCar1.get_is_police()
workCar1.show_speed()
workCar1.turn("right")

workCar2 = WorkCar("ZIL", "yellow", 40)
workCar2.get_color()
workCar2.go()
workCar2.stop()
workCar2.get_is_police()
workCar2.show_speed()
workCar2.turn("back")

townCar1 = TownCar("Mini", "blue", 70)
townCar1.get_color()
townCar1.go()
townCar1.stop()
townCar1.get_is_police()
townCar1.show_speed()
townCar1.turn("right")

townCar2 = TownCar("Smart", "yellow", 50)
townCar2.get_color()
townCar2.go()
townCar2.stop()
townCar2.get_is_police()
townCar2.show_speed()
townCar2.turn("back")

sportCar = SportCar("Ferrari", "red")
sportCar.get_color()
sportCar.go()
sportCar.stop()
sportCar.get_is_police()
sportCar.show_speed()
sportCar.turn("right")

policeCar = PoliceCar("Ford", "blue", 70)
policeCar.get_is_police()
policeCar.go()
policeCar.get_color()
policeCar.stop()
policeCar.show_speed()
policeCar.turn("back")

