from random import *
print("Привет! ТЫ попал в игру угадай число")
print("Тебе нужно угадать число от 1 до 100 Удачи")
n = randint(1,100)
print("Выбери сложность: ")
print("---1. Легко(10 попыток)")
print("---2. Легко(7 попыток)")
print("---3. Легко(4 попытки)")
user = int(input("Вебри сложность 1-2-3 "))
if user == 1:
    attemps=10
elif user ==2:
    attemps=7
elif user ==3:
    attemps=4
else:
    print("Такой сложности нет!!!!!")
    print("ТОГДА ТЫ БУДЕШЬ ПРОХОДИТЬ ХАРДКОРД")
    attemps=2
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
