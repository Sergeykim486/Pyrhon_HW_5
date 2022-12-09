#  ■ ▓ ▒ ░ █ ↔ ► ▬ ◄ ┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ֍ ◄─
import random, os, sys
from colorama import init, Fore
from colorama import Back
from colorama import Style

candys = 117
p1 = 0
p2 = 0
sel = 0
step = 1
star = '◄►'
stiles = {'Menu': Back.GREEN, 'Score': Back.BLUE, 'wins': Back.RED, 'Reset': Style.RESET_ALL, 'Input': Fore.YELLOW}

def main_menu():
    global stiles, candys, p1, p2, sel, star, step
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
    global stiles, candys, p1, p2, sel, star, step
    os.system('cls')
    if step == 1:
        s1 = '♦ '
        s2 = '  '
        star = '◄─'
    elif step == 2:
        s2 = '♦ '
        s1 = '  '
        star = '─►'
    print(stiles['Score'] + ''
          f'██████████████████████████████████████████████\n'
          f'██                                          ██\n'
          f'██   CANDYS: ֍ {threesim(str(candys))}                          ██\n'
          f'██   ┌───────────────┐  ┌───────────────┐   ██\n'
          f'██   │ {s1}ИГРОК 1:    │  │ {s2}ИГРОК 2:    │   ██\n'
          f'██   ├───────────────┤{star}├───────────────┤   ██\n'
          f'██   │ ֍ - {threesim(str(p1))}       │  │ ֍ - {threesim(str(p2))}       │   ██\n'
          f'██   └───────────────┘  └───────────────┘   ██\n'
          f'██                                          ██\n'
          f'██████████████████████████████████████████████\n'
          ''+ stiles['Reset'])

def threesim(x):
    if len(x) == 1:
        x = x + '  '
    elif len(x) == 2:
        x = x + ' '
    return x

def comp_step():
    global stiles, candys, p1, p2, sel, star, step
    while True:
        if candys <= 28:
            candy = candys
        else:
            candy = random.randint(1, 28)
        if 0 < candy <= 28 and candy <= candys:
            print(f'Игрок 2 взял {candy} конфет')
            return candy

def player_step():
    global stiles, candys, p1, p2, sel, star, step
    while True:
        candy = int(input('Сколько конфет вы хотите взять ->  '))
        if 0 < candy <= 28 and candy <= candys:
            return candy
        else:
            print(f'Вы не можете взять {candy}шт.!')

def new_game():
    global stiles, candys, p1, p2, sel, star, step
    candys = 117
    p1 = 0
    p2 = 0
    step = random.randint(1, 3)
    while candys > 0:
        print_score()
        if step == 1 or (step == 2 and sel == 2):
            take = player_step()
            candys = candys - take
            p1 = p1 + take + p2
            p2 = 0
            step = 2
        elif step == 2 and sel == 1:
            take = comp_step()
            candys = candys - take
            p2 = p2 + take + p1
            p1 = 0
            step = 1
    wins()

def wins():
    global stiles, candys, p1, p2, sel, star, step
    if p1 > 0:
        w = 1
    elif p2 > 0:
        w = 2
    os.system('cls')
    print(stiles['Input'] + ''
          f'██████████████████████████████████████████████\n'
          f'██                                          ██\n'
          f'██   C A N D Y S                            ██\n'
          f'██   ПОЗДРАВЛЯЕМ!!!                         ██\n'
          f'██                                          ██\n'
          f'██   ПОБЕДИЛ:                               ██\n'
          f'██                                          ██\n'
          f'██   И Г Р О К  {w}                           ██\n'
          f'██                                          ██\n'
          f'██████████████████████████████████████████████\n'
          f''+ stiles['Reset'])
    input(stiles['Reset'] + 'Чтобы продолжить нажмите [ENTER]')
    main_menu()

main_menu()