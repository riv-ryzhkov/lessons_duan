import sys
from key import themes
from key import reply

print("Добро пожаловать в Игру «Поле чудес»!!!")
print("-" * 50)

inlet = int(input("Введите пожалуйста любое число от 1 до 6: ->"))
if inlet not in themes:
    print("Вы ввели число не в диапазоне от 1 до 6!!!!!!\nПожалуйста введите в деапазоне от 1 до 6")
    inlet = int(input("Введите пожалуйста любое число от 1 до 6: ->"))

slovo = reply[inlet]
print("Вопрос:", themes[inlet])

tfies = 3
display = "_" * len(slovo)

game_over = False
while not game_over:
    print("У вас есть ❤", tfies, "попытки.")
    print(display)
    guess = input("Введите букву:->").upper()
    i = 0
    if guess in slovo:
        while slovo.find(guess, i) != -1:
            i = slovo.find(guess)
            display = display[:i] + guess + display[i + 1:]
            i += 1
        print("Поздравляем вы отгадали букву->"+ '|'+ guess +'|')
    else:
        # slovo == display
        print("Не правильная буква ->" + '|'+ guess +'|')
        tfies -=1

    if slovo == display:
        print("Поздравляем вы отгадали слово "+'«'+slovo+'»'+" \nИгра окончена.")
        game_over = True
    while tfies == 0:
            print("Игра окончена, у вас осталось ❤",tfies," попыток!!!")
            sys.exit()





