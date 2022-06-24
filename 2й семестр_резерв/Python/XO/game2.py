start = input('Игра "Крестики нолики"\nНажмите Enter, чтобы начать игру\n')


# Создаём игровое поле 3x3 в виде списка
field = []
for i in range(3):
    field.append(['.','.','.'])


# Функция предоставления игрового поля 3x3
def show(field):
    for i in range(3):
        print(*field[i])


# Функция проверки на корректный ввод координат для клетки
def valid(symbols):
    # Ставим условие на ввод пользователем координат учитывая пробел
    if len(symbols) != 3 or symbols[1] != " " or not symbols[0].isdigit() or not symbols[2].isdigit():
        show(field)
        print('Пожалуйста, введите корректные координаты\nИспользуйти цифры 1,2,3 и между ними пробел')
        return False
    # Ставим условие на ввод игроками цифр только 1,2,3. В списке цифры находятся под индексами 0 и 2
    vertical = int(symbols[0])
    horizontal = int(symbols[2])
    if vertical < 1 or vertical > 3 or horizontal < 1 or horizontal > 3:
        show(field)
        print('Данной строки и столбца нет, введите числа от 1 до 3:')
        return False
    # Уведомляем если поле уже занято 
    if field [vertical-1][horizontal-1] != '.':
        show(field)
        print('Эта клетка уже занята, выберите другие координаты')
        return False
    return True


# Функция обработки заполнения клеток (ввода координат)
# С помощью .split() индекс координаты по горизонтали сьезжает на 1.
def step(field, cell):
    while True:
        params = input('Введите номер строки и столбца:')
        if valid(params):
            params = params.split()
        else:
            continue
        if cell == 1:
            field[int(params[0])-1] [int(params[1])-1] = 'x'
        else:
            field[int(params[0])-1] [int(params[1])-1] = '0'
        return field


# Функция проверки на выигрыш
def check(position):
    for win in ['x', '0']:
        # выйгрыш по вертикали:
        if position[0][0] == position[1][0] == position[2][0] == win or position[0][1] == position[1][1] == position[2][1] == win or position[0][2] == position[1][2] == position[2][2] == win:
            return True
        # горизонтальный выйгрыш:
        if position[0][0] == position[0][1] == position[0][2] == win or position[1][0] == position[1][1] == position[1][2] == win or position[2][0] == position[2][1] == position[2][2] == win:
            return True
        # выйгрыши по диагонали
        if position[0][0] == position[1][1] == position[2][2] == win or position[0][2] == position[1][1] == position[2][0] == win:
            return True
    return False


# По умолчанию cell = -1 Если пустых полей нет - это значит ничья
# Если при подсчёте не будет обнаружено свободных клеток, то cell принимает значение ноль.
cell = -1
finish = False
while finish == False:
    sum = 0
    for i in range(3):
        sum += field[i].count('.')
    if sum == 0:
        cell = 0

    # При условии что все клетки заполнены ИЛИ произошел выигрыш - игра завершается
    if check(field) or cell == 0:
        finish = True
        break
    # в противном случае игра продолжается, а cell умножается на -1
    cell *= -1
    show(field)

    # Условие порядка хода крестика или нолика.   Например:
    # при умножении (-1)на(-1) будет = 1, то ходит крестик
    # при умножении 1 на (-1) будет = -1, то ходит "нолик"
    if cell == 1:
        print('Ход первого игрока с "x": ')
    else:
        print('Ход второго игрока с "0": ')
    step(field, cell)


# Условия результатов в конце игры
if not cell:
    print('Ничья')
elif cell == 1:
    print('Выигрыш первого игрока с "x"!!!')
else:
    print('Выигрыш второго игрока с "0"!!!')
# match cell:
#     case 1:
#         print('Выигрыш первого игрока с "x"!!!')
#     case 0:
#         print('Ничья')
#     case -1:
#         print('Выигрыш второго игрока с "0"!!!')
show(field)
