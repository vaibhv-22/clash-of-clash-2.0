from cProfile import label
from turtle import color
from matplotlib.pyplot import fill
# from goto import goto, comefrom, label
from numpy import char
from pyparsing import col
from input import *
import os
from colorama import Fore, Back, Style
from src.header import *
from src.init2 import *
from src.buildings import *
from src.king import *
from src.spell import *
from src.troops import *
from src.print_base import *

def builds(objecttype):
    objecttype.build()

os.system("clear")

start()
avatar = ""
while True:
    # Removing Cursor from Terminal     
    os.system("tput civis")
    if Not_Started == True:
        print("PRESS K to use King and Q to use QUEEN")
        x = Get()
        queen = Get.__call__(x)
        Not_Started = False
        avatar = queen.lower()
    x = Get()
    called = input_to(x)
    if int(time.time()) == int(ATTACKTIME[0]):
        Queen_Special_Attack(ATTACK_DATA[0],ATTACK_DATA[1],ATTACK_DATA[2],ATTACK_DATA[3],ATTACK_DATA[4],ATTACK_DATA[5],ATTACK_DATA[6],ATTACK_DATA[7],ATTACK_DATA[8],ATTACK_DATA[9],ATTACK_DATA[10])

    if called == 'q':
        break
    elif called == 'a' or called == 'd' or called == 'w' or called == 's':
        king.move(king_pos, huts ,cannons,wizard_towers ,called, all_troops)
        last_direction = called   
    elif called == ' ' or called == ';':
        king.attack(town_hall, king_pos, huts,cannons,wizard_towers ,called, all_troops,all_walls,last_direction,avatar)
    elif called == 'h' or called == 'r':
        spell = Spell(called)
        spell.cast(king,all_troops)
    elif (called =='i' or called == 'o' or called == 'p') and cnt_troops[0] < limit_trp[0]:
        cnt_troops[0] += 1
        for i in cannons:
            i.attack(king,king_pos, all_troops)
        for i in wizard_towers:
            i.attack(king,king_pos, all_troops)
        troop_gen = Barb(called)
        all_troops.append(troop_gen)
        troop_gen.build(called)
    elif (called =='j' or called == 'k' or called == 'l') and cnt_troops[1] < limit_trp[1]:
        cnt_troops[1] += 1
        for i in cannons:
            i.attack(king,king_pos, all_troops)
        for i in wizard_towers:
            i.attack(king,king_pos, all_troops)
        troop_gen = Archer(called)
        all_troops.append(troop_gen)
        troop_gen.build(called)
    elif (called =='b' or called == 'n' or called == 'm') and cnt_troops[2] < limit_trp[2]:
        cnt_troops[2] += 1
        for i in cannons:
            i.attack(king,king_pos, all_troops)
        for i in wizard_towers:
            i.attack(king,king_pos, all_troops)
        troop_gen = Ballon(called)
        all_troops.append(troop_gen)
        troop_gen.build(called)
    elif called == None:
        for i in cannons:
            i.attack(king,king_pos, all_troops)
        for i in wizard_towers:
            i.attack(king,king_pos, all_troops)
    os.system("clear")

    # Entry for the Foreign Troops -> Barbarian
    board[4][0] = 'i'
    board[3][WIDTH_BASE-1] = 'o'
    board[1][16] = 'p'
    # Entry for the Foreign Troops -> Archer
    board[14][0] = 'j'
    board[13][WIDTH_BASE-1] = 'k'
    board[1][36] = 'l'
    # Entry for the Foreign Troops -> Balloons
    board[24][0] = 'b'
    board[23][WIDTH_BASE-1] = 'n'
    board[1][56] = 'm'


    # Building all the buildings
    for i in list_buildings:
        i.build()

    # KING    
    king.build()    
    # for cannon in cannons:
    #     cannon.build()
    # Moving the troops for this loop
    for trp in all_troops:
        # trp.build()
        trp.move(huts,cannons,list_buildings,all_walls,wizard_towers)
    for wl in all_walls:
        wl.build()



    k = printing_base(avatar)
    if k == -1:
        break
    elif k == 2:
        # change_level_to_2()
        Level2()
        # global CURRENT_LEVEL
        # CURRENT_LEVEL += 1
        
        
    elif k == 3:
        Level3()
        # CURRENT_LEVEL += 1
    for x in range(HEIGHT_BASE):
        for y in range(WIDTH_BASE):
            colr[x][y] = ' '





