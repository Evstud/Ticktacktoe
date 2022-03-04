import sys

R = 4
C = 4
matrix = [
    [' ', 0, 1, 2],
    [0, '-', '-', '-'],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
]
dash = '-'


def inp_x():
    x = (int(input("(Для х) Введите номер строчки: "))) + 1
    y = (int(input("(Для х) Введите номер стролбика: "))) + 1
    if matrix[x][y] != '-':
        print("Ход сюда уже был сделан, повторите ввод")
        inp_x()
    else:
        matrix[x][y] = 'x'
        checking()
    return inp_x


def inp_o():
    x = (int(input("(Для о) Введите номер строчки: "))) + 1
    y = (int(input("(Для о) Введите номер столбика: "))) + 1
    if matrix[x][y] != '-':
        print("Ход сюда уже был сделан, повторите ввод")
    else:
        matrix[x][y] = 'o'
        checking()
    return inp_o


def current_result():
    for i in range(R):  # строки
        for j in range(C):  # столбцы
            print(matrix[i][j], ' ', end="")
        print()
    return current_result


def checking():
    win1 = [matrix[1][1], matrix[1][2], matrix[1][3]]
    win2 = [matrix[2][1], matrix[2][2], matrix[2][3]]
    win3 = [matrix[3][1], matrix[3][2], matrix[3][3]]
    win4 = [matrix[1][1], matrix[2][1], matrix[3][1]]
    win5 = [matrix[1][2], matrix[2][2], matrix[3][2]]
    win6 = [matrix[1][3], matrix[2][3], matrix[3][3]]
    win7 = [matrix[1][1], matrix[2][2], matrix[3][3]]
    win8 = [matrix[1][3], matrix[2][2], matrix[3][1]]
    win_x = ['x', 'x', 'x']
    win_o = ['o', 'o', 'o']

    if win1 == win_x or win2 == win_x or win3 == win_x or win4 == win_x or win5 == win_x or win6 == win_x or win7 == win_x or win8 == win_x:
        current_result()
        print("x won")
        sys.exit()
    elif win1 == win_o or win2 == win_o or win3 == win_o or win4 == win_o or win5 == win_o or win6 == win_o or win7 == win_o or win8 == win_o:
        current_result()
        print("o won")
        sys.exit()


def checking2():
    checking_list = []
    for c in matrix:
        checking_list.extend(c)
    if dash not in checking_list:
        print("Draw")
        sys.exit()


current_result()

while True:
    inp_x()
    current_result()
    checking()
    checking2()
    inp_o()
    current_result()
    checking()
    checking2()
