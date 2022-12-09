#  ■ ▓ ▒ ░ █ ↔ ► ▬ ◄ ┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ֍ ◄─ ┼
import random, os, sys, time
from colorama import init, Fore
from colorama import Back
from colorama import Style

stiles = {'Menu': Back.GREEN, 'Score': Back.BLUE, 'nonwin': Back.RED, 'Reset': Style.RESET_ALL, 'wins': Fore.GREEN}
xo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
wincom = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
p = 0
sel = 0
step = 0

def main_menu():
    global stiles, xo, p, sel
    os.system('cls')
    print(stiles['Menu'] + ''
          '██████████████████████████████████████████████\n'
          '██                                          ██\n'
          '██   C A N D Y S                            ██\n'
          '██   Главвное меню                          ██\n'
          '██                                          ██\n'
          '██   [1] - Один игрок (против компьютера)   ██\n'
          '██   [2] - Два игрока                       ██\n'
          '██   [3] - Выход                            ██\n'
          '██                                          ██\n'
          '██████████████████████████████████████████████\n'
          ''+ stiles['Reset'])
    while True:
        sel = int(input('Выберите действие ->  '))
        if 0 < sel < 4:
            if sel == 1 or sel == 2:
                new_game()
            elif sel == 3:
                sys.exit()
        else:
            print('Не верный выбор.')

def print_score():
    global stiles, xo, p, sel, step
    os.system('cls')
    print(stiles['Score'] + ''
          f'██████████████████████████████████████████████\n'
          f'██     0   1   2                            ██\n'
          f'██   ┌───┬───┬───┐   ║   ИГРОК {step}:           ██\n'
          f'██ 0 │ {xo[0][0]} │ {xo[0][1]} │ {xo[0][2]} │   ║   ВАШ ХОД...         ██\n'
          f'██   ├───┼───┼───┤   ║   ________________   ██\n'
          f'██ 1 │ {xo[1][0]} │ {xo[1][1]} │ {xo[1][2]} │   ║                      ██\n'
          f'██   ├───┼───┼───┤   ║                      ██\n'
          f'██ 2 │ {xo[2][0]} │ {xo[2][1]} │ {xo[2][2]} │   ║                      ██\n'
          f'██   └───┴───┴───┘                          ██\n'
          f'██████████████████████████████████████████████\n'
          ''+ stiles['Reset'])

def comp_step():
    global stiles, xo, p, sel
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if xo [x][y] == ' ':
            res = [x,y]
            return res

def player_step():
    global stiles, xo, p, sel
    while True:
        coordinatein = str(input('Введите координаты в формате 0,0 или 0.0 - строка, столбец ->  '))
        coordinatein = coordinatein.replace('.', ',')
        coordinates = []
        for i in coordinatein:
            if i!= ',':
                coordinates.append(int(i))
        if xo [coordinates[0]][coordinates[1]] == ' ':
            return coordinates

def new_game():
    global stiles, xo, p, sel, step
    xo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    step = random.randint(1, 2)
    while True:
        find = 0
        if checkwiner() == 0:
            print_score()
            for i in range(3):
                for j in range(3):
                    if xo [i][j] == ' ':
                        find = 1
            if find == 1:
                if step == 1:
                    curstep = player_step()
                    xo [curstep[0]][curstep[1]] = 'x'
                    step = 2
                elif step == 2 and sel == 1:
                    time.sleep(3)
                    curstep = comp_step()
                    xo [curstep[0]][curstep[1]] = '0'
                    step = 1
                elif step == 2 and sel == 2:
                    curstep = player_step()
                    xo [curstep[0]][curstep[1]] = '0'
                    step = 1
            else:
                wins()
        else:
            wins()

def wins():
    global stiles, xo, p, sel
    os.system('cls')
    if p == 0:
        winner = 'НИЧЬЯ!  '
        text = '              '
        st = stiles['nonwin']
    elif p == 1:
        winner = 'ИГРОК 1:'
        text = 'ВЫ ВЫЙГРАЛИ!!!'
        st = stiles['wins']
    elif p == 2:
        winner = 'ИГРОК 2:'
        text = 'ВЫ ВЫЙГРАЛИ!!!'
        st = stiles['wins']
    print(st + ''
          f'██████████████████████████████████████████████\n'
          f'██     0   1   2                            ██\n'
          f'██   ┌───┬───┬───┐   ║   {winner}           ██\n'
          f'██ 0 │ {xo[0][0]} │ {xo[0][1]} │ {xo[0][2]} │   ║   {text}     ██\n'
          f'██   ├───┼───┼───┤   ║   ________________   ██\n'
          f'██ 1 │ {xo[1][0]} │ {xo[1][1]} │ {xo[1][2]} │   ║                      ██\n'
          f'██   ├───┼───┼───┤   ║                      ██\n'
          f'██ 2 │ {xo[2][0]} │ {xo[2][1]} │ {xo[2][2]} │   ║                      ██\n'
          f'██   └───┴───┴───┘                          ██\n'
          f'██████████████████████████████████████████████\n'
          ''+ stiles['Reset'])
    input(stiles['Reset'] + 'Чтобы продолжить нажмите [ENTER]')
    main_menu()

def checkwiner():
    global stiles, xo, p, sel, wincom
    winspos = []
    for i in range(3):
        for j in range(3):
            winspos.append(xo[i][j])
    p = 0
    for item in wincom:
        if winspos[item[0]] == 'x' and winspos[item[1]] == 'x' and winspos[item[2]] == 'x':
            p = 1
        elif winspos[item[0]] == '0' and winspos[item[1]] == '0' and winspos[item[2]] == '0':
            p = 2
    return p

main_menu()