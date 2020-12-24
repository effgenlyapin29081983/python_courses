class MyDate():
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    """
    Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода.
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
    """

    @classmethod
    def getDateNum(cls, dateStr):
        cls.date = dateStr.split("-")
        cls.day = cls.date[0]
        cls.month = cls.date[1]
        cls.year = cls.date[2]

    @staticmethod
    def validDate(day, month, year):
        valid = True
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            valid = False
        elif int(month)<1 or int(month)>12:
            valid = False
        elif int(day) < 1 or int(day) > MyDate.days[int(month)-1]:
            valid = False

        if valid:
            print(f"{day}:{month}:{year} is valid Date")
        else:
            print(f"{day}:{month}:{year} is invalid Date")


MyDate.getDateNum("29-02-2020")
MyDate.validDate(MyDate.day, MyDate.month, MyDate.year)