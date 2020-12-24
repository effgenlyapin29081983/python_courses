class MyException(Exception):
    """
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
    Проверьте его работу на данных, вводимых пользователем.
    При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
    """
    def __init__(self, text):
        print(text)

try:
    delitel = int(input("Enter delitel:\n"))
    if delitel == 0:
        raise MyException("My divizion by zero!")
except MyException:
    pass

