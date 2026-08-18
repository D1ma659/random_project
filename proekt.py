from random import *
print("Привет! ТЫ попал в игру угадай число")
print("Тебе нужно угадать число от 1 до 100 УДачи")
n = randint(1,100)
attemps=7
while attemps > 0:
    user=int(input("Введи число: "))
    attemps = attemps - 1
    if user == n:
        print("ты угадал")
        break
    else:
        print("Неверно")
        if user < n:
            print("Число больше")
        else:
            print("Число меньше")
    print("Осталось попыток",attemps)
print("Игра окончена")
print("Загаданное число",n)