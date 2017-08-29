import os


firstTower = []
secondTower = []
thirdTower = [8, 7, 6, 5, 4, 3, 2, 1]

commandsList = ['exit', 'e', 'move', 'm', 'help', 'h']
current_error = 'none'


def check_values(fr, to):
    if fr == 1:
        if to == 2:
            if not secondTower:
                return True
            else:
                if secondTower[len(secondTower) - 1] < firstTower[len(firstTower) - 1]:
                    return False
                else:
                    return True
        elif to == 3:
            if not thirdTower:
                return True
            else:
                if thirdTower[len(thirdTower) - 1] < firstTower[len(firstTower) - 1]:
                    return False
                else:
                    return True
    elif fr == 2:
        if to == 1:
            if not firstTower:
                return True
            else:
                if firstTower[len(firstTower) - 1] < secondTower[len(secondTower) - 1]:
                    return False
                else:
                    return True
        elif to == 3:
            if not thirdTower:
                return True
            else:
                if thirdTower[len(thirdTower) - 1] < secondTower[len(secondTower) - 1]:
                    return False
                else:
                    return True
    elif fr == 3:
        if to == 1:
            if not firstTower:
                return True
            else:
                if firstTower[len(firstTower) - 1] < thirdTower[len(thirdTower) - 1]:
                    return False
                else:
                    return True
        elif to == 2:
            if not secondTower:
                return True
            else:
                if secondTower[len(secondTower) - 1] < thirdTower[len(thirdTower) - 1]:
                    return False
                else:
                    return True


def is_tower_empty(tow):
    if tow == 1:
        if firstTower:
            return False
        else:
            return True
    elif tow == 2:
        if secondTower:
            return False
        else:
            return True
    elif tow == 3:
        if thirdTower:
            return False
        else:
            return True


def check_num(num, tow):
    if num == 1:
        if tow == 1:
            if 1 in firstTower:
                return 1
        elif tow == 2:
            if 1 in secondTower:
                return 1
        elif tow == 3:
            if 1 in thirdTower:
                return 1
    elif num == 2:
        if tow == 1:
            if 2 in firstTower:
                return 1
        elif tow == 2:
            if 2 in secondTower:
                return 1
        elif tow == 3:
            if 2 in thirdTower:
                return 1
    elif num == 3:
        if tow == 1:
            if 3 in firstTower:
                return 1
        elif tow == 2:
            if 3 in secondTower:
                return 1
        elif tow == 3:
            if 3 in thirdTower:
                return 1
    elif num == 4:
        if tow == 1:
            if 4 in firstTower:
                return 1
        elif tow == 2:
            if 4 in secondTower:
                return 1
        elif tow == 3:
            if 4 in thirdTower:
                return 1
    elif num == 5:
        if tow == 1:
            if 5 in firstTower:
                return 1
        elif tow == 2:
            if 5 in secondTower:
                return 1
        elif tow == 3:
            if 5 in thirdTower:
                return 1
    elif num == 6:
        if tow == 1:
            if 6 in firstTower:
                return 1
        elif tow == 2:
            if 6 in secondTower:
                return 1
        elif tow == 3:
            if 6 in thirdTower:
                return 1
    elif num == 7:
        if tow == 1:
            if 7 in firstTower:
                return 1
        elif tow == 2:
            if 7 in secondTower:
                return 1
        elif tow == 3:
            if 7 in thirdTower:
                return 1
    elif num == 8:
        if tow == 1:
            if 8 in firstTower:
                return 1
        elif tow == 2:
            if 8 in secondTower:
                return 1
        elif tow == 3:
            if 8 in thirdTower:
                return 1
    return 0


def move(fr, to):
    if fr == 1:
        if to == 2:
            secondTower.append(firstTower.pop())
        elif to == 3:
            thirdTower.append(firstTower.pop())
    elif fr == 2:
        if to == 1:
            firstTower.append(secondTower.pop())
        elif to == 3:
            thirdTower.append(secondTower.pop())
    elif fr == 3:
        if to == 1:
            firstTower.append(thirdTower.pop())
        elif to == 2:
            secondTower.append(thirdTower.pop())


def current_situation():
    os.system('clear')
    print('Current situation:\t', 'Error: ', current_error, sep='', end='\n\n')
    print('Tower #1: ', '8' * check_num(8, 1), '7' * check_num(7, 1), '6' * check_num(6, 1), '5' * check_num(5, 1),
          '4' * check_num(4, 1), '3' * check_num(3, 1), '2' * check_num(2, 1), '1' * check_num(1, 1), sep='',
          end='\n\n')
    print('Tower #2: ', '8' * check_num(8, 2), '7' * check_num(7, 2), '6' * check_num(6, 2), '5' * check_num(5, 2),
          '4' * check_num(4, 2), '3' * check_num(3, 2), '2' * check_num(2, 2), '1' * check_num(1, 2), sep='',
          end='\n\n')
    print('Tower #3: ', '8' * check_num(8, 3), '7' * check_num(7, 3), '6' * check_num(6, 3), '5' * check_num(5, 3),
          '4' * check_num(4, 3), '3' * check_num(3, 3), '2' * check_num(2, 3), '1' * check_num(1, 3), sep='',
          end='\n\n')


def game_cycle():
    while secondTower != [8, 7, 6, 5, 4, 3, 2, 1]:
        global current_error
        next_turn = input('\nEnter the next command:  ')
        if next_turn not in commandsList:
            current_error = 'Command does not exist'
            continue
        else:
            current_error = 'none'
        if next_turn == 'exit' or next_turn == 'e':
            exit()
        elif next_turn == 'move' or next_turn == 'm':
            try:
                f = int(input('\nFrom which tower you want to move disc?  '))
            except ValueError:
                current_error = 'Value Error'
                current_situation()
                continue
            if is_tower_empty(f):
                current_error = 'Chosen tower is empty'
                current_situation()
                continue
            try:
                t = int(input('\nTo which tower you want to move disc?  '))
            except ValueError:
                current_error = 'Value Error'
                current_situation()
                continue
            if t == f:
                current_error = 'You can\'t move to this tower'
                current_situation()
                continue
            if check_values(f, t):
                move(f, t)
            else:
                current_error = 'You can\'t do this'
                current_situation()
                continue
        elif next_turn == 'help' or next_turn == 'h':
            print('\n', 'move(m) - move disc from one tower to another', 'exit(e) - exit from program',
                  'help(h) - prints help', sep='\n', end='\n\n')
            wait = input()
            del wait
        current_situation()

current_situation()
game_cycle()
