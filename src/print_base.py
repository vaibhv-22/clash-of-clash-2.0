from time import sleep
from colorama import Fore, Back, Style
from .header import *
from .buildings import *
from .init2 import *
from .king import *

def printing_base(avatar):
    lol = []
    for i in range(HEIGHT_BASE):
        for j in range(WIDTH_BASE):
            if colr[i][j] == "WIZARD_TOWER":
                lol.append(Back.MAGENTA)
            if colr[i][j] == "BLUE":
                lol.append(Back.BLUE)
            if colr[i][j] == "WHITE":
                lol.append(Back.LIGHTWHITE_EX)
            if len(filled[i][j]) > 0 and filled[i][j][0] == 'B':
                lol.append(board[i][j])
            elif board[i][j] == '#':
                if town_hall.health > HEALTH_TOWN/2:
                    lol.append(Fore.GREEN + board[i][j])
                elif town_hall.health > HEALTH_TOWN/4:
                    lol.append(Fore.YELLOW + board[i][j])
                else:
                    lol.append(Fore.RED + board[i][j])
                lol.append(Fore.RESET)
            elif board[i][j] == 'C':
                if cannons[(int)(filled[i][j][0])].power_on == True:
                    lol.append(Back.WHITE)
                if cannons[(int)(filled[i][j][0])].health > HEALTH_CANNON/2:
                    lol.append(Fore.GREEN + board[i][j])
                    lol.append(Fore.RESET)
                elif cannons[(int)(filled[i][j][0])].health > HEALTH_CANNON/4:
                    lol.append(Fore.YELLOW + board[i][j])
                    lol.append(Fore.RESET)
                else:
                    lol.append(Fore.RED + board[i][j])
                    lol.append(Fore.RESET)
                lol.append(Back.RESET)
            elif board[i][j] == 'Z':
                if wizard_towers[(int)(filled[i][j][0])].power_on == True:
                    lol.append(Back.WHITE)
                if wizard_towers[(int)(filled[i][j][0])].health > HEALTH_CANNON/2:
                    lol.append(Fore.GREEN + board[i][j])
                    lol.append(Fore.RESET)
                elif wizard_towers[(int)(filled[i][j][0])].health > HEALTH_CANNON/4:
                    lol.append(Fore.YELLOW + board[i][j])
                    lol.append(Fore.RESET)
                else:
                    lol.append(Fore.RED + board[i][j])
                    lol.append(Fore.RESET)
                lol.append(Back.RESET)
            elif board[i][j] == '_' or board[i][j] == '/' or board[i][j] == '\\' or board[i][j] == '|':
                # global huts
                # lol.append(len(filled[i][j]), len(huts))
                if huts[(int)(filled[i][j][0])].health > HEALTH_HUT/2:
                    lol.append(Fore.GREEN + board[i][j])
                    lol.append(Fore.RESET)
                elif huts[(int)(filled[i][j][0])].health > HEALTH_HUT/4:
                    lol.append(Fore.YELLOW + board[i][j])
                    lol.append(Fore.RESET)
                else:
                    lol.append(Fore.RED + board[i][j])
                    lol.append(Fore.RESET)
            elif len(filled[i][j]) > 0 and filled[i][j][0] == 'w':
                lol.append(Fore.BLUE + Back.LIGHTMAGENTA_EX + 'W')
                lol.append(Fore.RESET)
                lol.append(Back.RESET)
            else:
                if board[i][j] == "K" and avatar == "q":
                    lol.append("Q")
                else:
                    lol.append(board[i][j])
            if colr[i][j] == "WIZARD_TOWER":
                lol.append(Back.RESET)
            if colr[i][j] == "BLUE" or colr[i][j] == "WHITE":
                lol.append(Fore.RESET + Back.RESET)
        lol.append("\n")
    print("".join(lol))
    sum = 0
    for wl in all_walls:
        sum = wl.health + sum
    healthDisplay = ' ' * int(king.health*10/HEALTH_KING)  
    remainingDisplay = ' ' * (10 - int(king.health*10/HEALTH_KING))
    if avatar == 'k':
        print("King's Health : |", end='')
    else:
        print("Queen's Health : |", end='') 
    print(Back.GREEN + healthDisplay + Back.RED + remainingDisplay + Back.RESET + "|" )  # Print out textbased healthbar
    total_building = 0
    for i in list_buildings:
        if i.health > 0:
            total_building += 1
    global CURRENT_LEVEL
    if total_building == 0 and CURRENT_LEVEL == 1:
        CURRENT_LEVEL += 1
        print(r"""
             _      ____  _     _  _      _____   _____  ____    _     _____ _     _____ _       ____ 
            / \__/|/  _ \/ \ |\/ \/ \  /|/  __/  /__ __\/  _ \  / \   /  __// \ |\/  __// \     /_   \
            | |\/||| / \|| | //| || |\ ||| |  _    / \  | / \|  | |   |  \  | | //|  \  | |      /   /
            | |  ||| \_/|| \// | || | \||| |_//    | |  | \_/|  | |_/\|  /_ | \// |  /_ | |_/\  /   /_
            \_/  \|\____/\__/  \_/\_/  \|\____\    \_/  \____/  \____/\____\\__/  \____\\____/  \____/
            """)       
        sleep(4)          
        return 2
    elif total_building == 0 and CURRENT_LEVEL == 2:
        CURRENT_LEVEL += 1
        print(r"""
             _      ____  _     _  _      _____   _____  ____    _     _____ _     _____ _      _____ 
            / \__/|/  _ \/ \ |\/ \/ \  /|/  __/  /__ __\/  _ \  / \   /  __// \ |\/  __// \     \__  \
            | |\/||| / \|| | //| || |\ ||| |  _    / \  | / \|  | |   |  \  | | //|  \  | |       /  |
            | |  ||| \_/|| \// | || | \||| |_//    | |  | \_/|  | |_/\|  /_ | \// |  /_ | |_/\   _\  |
            \_/  \|\____/\__/  \_/\_/  \|\____\    \_/  \____/  \____/\____\\__/  \____\\____/  /____/                                                                            
            """)                 
        sleep(4)          
        return 3
    elif total_building == 0 and CURRENT_LEVEL == 3:
        print(r"""
            ___  _ ____  _       _      ____  _     
            \  \///  _ \/ \ /\  / \  /|/  _ \/ \  /|
             \  / | / \|| | ||  | |  ||| / \|| |\ ||
             / /  | \_/|| \_/|  | |/\||| \_/|| | \||
            /_/   \____/\____/  \_/  \|\____/\_/  \|
            """)                 
        return -1
    total_troops_health = 0
    for i in all_troops:
        if i.health <= 0:
            i.health = 0
        total_troops_health += i.health
    if king.health <= 0 and total_troops_health <= 0:
        print(r"""
            ___  _ ____  _       _     ____  ____  _____
            \  \///  _ \/ \ /\  / \   /  _ \/ ___\/  __/
             \  / | / \|| | ||  | |   | / \||    \|  \  
             / /  | \_/|| \_/|  | |_/\| \_/|\___ ||  /_ 
            /_/   \____/\____/  \____/\____/\____/\____\
        """)
        return -1


