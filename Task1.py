import random

p1 = 0
p2 = 0
Tab = 0
x = 0

def print_score():
    global p1, p2, Tab
    print(f'\n\n==================SCORE==================\n'
          f'                                         \n'
          f'        P1:  {p1}          P2:  {p2}           \n'
          f'                                         \n'
          f'=========================================\n')

def enterx():
    x = int(input(f'Сколько конфет вы берете со стола? (макс 28) ->  '))
    if 0 < x <= 28:
        return int(x)
    else:
        enterx()

def new_singl_game():
    global p1, p2, Tab
    p1 = 0
    p2 = 0
    Tab = 117
    fstep = random.randint(1, 2)
    while Tab > 0:
        print(f'НК СТОЛЕ ЛЕЖИТ {Tab} КОНФЕТ.\nИгрок {fstep}, Ваш ход...')
        x = enterx()
        if fstep == 1:
            p1 += x + p2
            p2 = 0
            fstep = 2
        else:
            p2 += x + p1
            p1 = 0
            fstep = 1
        Tab -= x
        print_score()

new_singl_game()