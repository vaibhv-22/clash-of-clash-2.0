from ctypes import sizeof
from glob import glob
from .header import *
from .buildings import *
from .king import King
from .troops import Troops

list_buildings = []
all_troops = []
town_hall_shape = [[i, j, '#'] for i in range(3) for j in range(5)]
town_hall = Buildings('Town Hall', 17, 68, town_hall_shape,0)
hut_pos = [[13, 57], [14, 80], [21, 58], [25, 75], [23, 83]]
hut_shape = [[0, 0, '_'], [1, -1, '/'], [1, 1, '\\'],
                [2, -1, '|'], [2, 0, '_'], [2, 1, '|']]
huts = []
cannon_pos = [[18,54] , [23, 73], [19, 85]]
cannon_shape = [[i, j, 'C'] for i in range(2) for j in range(3)]
cannons = []
wizard_tower_pos = [[25,68]]
wizard_tower_shape = [[i, j, 'Z'] for i in range(2) for j in range(2)]
wizard_towers = []
king_pos = [35,68]
king = King(king_pos)
troop = Troops([0,0])
Not_Started = True

def Level2():
    start()
    cannon_pos.append([33, 25])

def start():

    # global board, filled, filled2,colr
    # board = [[' ' for i in range(WIDTH_BASE)] for j in range(HEIGHT_BASE)]
    # filled = [['' for i in range(WIDTH_BASE)] for j in range(HEIGHT_BASE)]
    # filled2 = [['' for i in range(WIDTH_BASE)] for j in range(HEIGHT_BASE)]
    # colr = [[' ' for i in range(WIDTH_BASE)] for j in range(HEIGHT_BASE)]
    for i in range(WIDTH_BASE):
        board[0][i] = '-'
        board[1][i] = '-'
        board[HEIGHT_BASE-2][i] = '-'
        board[HEIGHT_BASE-1][i] = '-'
        filled[0][i] = 'BORDER'
        filled[1][i] = 'BORDER'
        filled[HEIGHT_BASE-2][i] = 'BORDER'
        filled[HEIGHT_BASE-1][i] = 'BORDER'
    for i in range(HEIGHT_BASE):
        board[i][0] = '|'
        board[i][WIDTH_BASE - 1] = '|'
        filled[i][0] = 'BORDER'
        filled[i][WIDTH_BASE - 1] = 'BORDER'


    all_troops.clear()
    # global list_buildings, town_hall
    town_hall = Buildings('Town Hall', 17, 68, town_hall_shape,0)
    list_buildings.clear()
    list_buildings .append(town_hall)
    town_hall.build()
    # global huts
    huts.clear()
    cnt = 0
    for i in hut_pos:
        hut = Buildings('hut',i[0],i[1],hut_shape,cnt)
        huts.append(hut)
        cnt+=1
        hut.build()
    for i in huts:
        list_buildings.append(i)

    # global cannons, cannon_pos
    # cannons = []
    cnt = 0
    for i in cannon_pos:
        cannon = Cannon("cannon",i[0],i[1],cannon_shape,cnt)
        cannons.append(cannon)
        cnt += 1
        cannon.build()
    for i in cannons:
        list_buildings.append(i)

    # global wizard_towers, wizard_tower_pos
    # wizard_towers = []
    cnt = 0
    for i in wizard_tower_pos:
        wizard_tower = Wizard_Tower("wt",i[0],i[1],wizard_tower_shape,cnt)
        wizard_towers.append(wizard_tower)
        cnt += 1
        wizard_tower.build() 
    for i in wizard_towers:
        list_buildings.append(i)

    # global king,troop
    king = King(king_pos)
    troop = Troops([0,0])
    # Buildings.TOTAL_BUILDING = 11


all_walls = []
for i in range(65, 76):
    Wall = Walls(15,i)
    all_walls.append(Wall)
    Wall = Walls(21,i)
    all_walls.append(Wall)
    filled[15][i] = 'walls'
    filled[21][i] = 'walls'
for i in range(15, 22):
    if i != 15 and i != 21:
        Wall = Walls(i,65)
        all_walls.append(Wall)
    if i != 15 and i != 21:
        Wall = Walls(i,75)
        all_walls.append(Wall)
    filled[i][65] = 'walls'
    filled[i][75] = 'walls'



