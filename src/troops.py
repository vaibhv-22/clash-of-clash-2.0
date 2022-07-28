from turtle import pos
from matplotlib.pyplot import fill
from numpy import Inf
from .header import *
from .buildings import *
from .init2 import *

class Troops:
    """Class to build attackers."""

    def __init__(self, called):
        """init2ializing class."""
        self.pos = [0,0]
        self.health = HEALTH_BARB
        self.speed = SPEED_BARB
        self.attack_power = ATTACK_POWER_BARB
    
        
    

class Barb(Troops):
    def __init__(self, called):
        super().__init__(called)
    def build(self,called):
        if(called == 'i'):
            self.pos = [4,1]
            board[4][1] = '*'
            filled[4][1] = 'troop'
        elif(called == 'p'):
            self.pos = [2,16]
            board[2][16] = '*'
            filled[2][16] = 'troop'
        elif(called == 'o'):
            self.pos = [3,WIDTH_BASE - 2]
            board[3][WIDTH_BASE - 2] = '*'
            filled[3][WIDTH_BASE - 2] = 'troop'
    
    def move(self, huts , cannons,list_buildings,all_walls,wizard_towers):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[self.pos[0]][self.pos[1]] = ' '
            dis = Inf
            for i in list_buildings:
                if i.health > 0:
                    for j in i.lists:
                        if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                            dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                            ind = i
                            indj = [i.pos_x + j[0],i.pos_y + j[1]]
            if dis != Inf:
                if(dis == 1 or (dis == 2 and indj[0] != self.pos[0] and indj[1] != self.pos[1])):
                    ind.health -= self.attack_power
                    # os.system('aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                    board[self.pos[0]][self.pos[1]] = '*'
                else:    
                    store_pos = self.pos[:]
                    if(indj[0] < self.pos[0]):
                        self.pos[0] -= 1
                    elif(indj[0] > self.pos[0]):
                        self.pos[0] += 1
                    elif (indj[1] < self.pos[1]):
                        self.pos[1] -= 1
                    elif(indj[1] > self.pos[1]):
                        self.pos[1] += 1
                    if(board[self.pos[0]][self.pos[1]] == 'W'):
                        # walls at that point health = 0
                        sum = 0
                        for wl in all_walls:
                            sum += wl.health
                        # NORMAL CASE
                        # if sum == 32:
                        for wl in all_walls:
                            if wl.pos_x == self.pos[0] and wl.pos_y == self.pos[1]:
                                wl.health = 0
                                wl.build()
                        # else:
                        #     self.pos = store_pos[:]
                        #     dis = Inf
                        #     ind = -1
                        #     for wl in all_walls:
                        #         if wl.health == 0:
                        #             if dis > abs(wl.pos_x - self.pos[0]) + abs(wl.pos_y - self.pos[1]):
                        #                 dis = abs(wl.pos_x - self.pos[0]) + abs(wl.pos_y - self.pos[1])
                        #                 ind = wl
                            # MOVEMENT AVOIDING WALLS
                            # self.pos
                            # ind -> all_walls[ind] -> destination
                            # self.pos -> current position
                            # if self.pos[0] < ind.pos_x and board[self.pos[0]+1][self.pos[1]] == ' ':
                            #     self.pos[0] += 1
                            # elif self.pos[0] > ind.pos_x and board[self.pos[0]-1][self.pos[1]] == ' ':
                            #     self.pos[0] -= 1
                            # elif self.pos[1] < ind.pos_y and board[self.pos[0]][self.pos[1]+1] == ' ':
                            #     self.pos[1] += 1
                            # elif self.pos[1] > ind.pos_y and board[self.pos[0]][self.pos[1]-1] == ' ':
                            #     self.pos[1] -= 1 
                            # if self.pos[0] == store_pos[0] and self.pos[1] == store_pos[1]:
                            #     if board[self.pos[0]][self.pos[1]+1] == 'W' and board[self.pos[0]+1][self.pos[1]+1] == 'W' and board[self.pos[0]+1][self.pos[1]+2] == 'W':
                            #         self.pos[0] += 1
                            #     if board[self.pos[0]][self.pos[1]-1] == 'W' and board[self.pos[0]-1][self.pos[1]-1] == 'W' and board[self.pos[0]-1][self.pos[1]-2] == 'W':
                            #         self.pos[0] -= 1
                            #     if board[self.pos[0]+1][self.pos[1]] == 'W' and board[self.pos[0]+1][self.pos[1]+1] == 'W' and board[self.pos[0]+2][self.pos[1]+1] == 'W':
                            #         self.pos[1] -= 1
                            #     if board[self.pos[0]-1][self.pos[1]] == 'W' and board[self.pos[0]-1][self.pos[1]-1] == 'W' and board[self.pos[0]-2][self.pos[1]-1] == 'W':
                            #         self.pos[1] += 1
                        
                    board[self.pos[0]][self.pos[1]] = '*'



class Archer(Troops):
    def __init__(self, called):
        super().__init__(called)
        self.health = HEALTH_ARC
        self.speed = SPEED_ARC
        self.attack_power = ATTACK_POWER_ARC
        self.range = RANGE_ARC
    def build(self,called):
        if(called == 'j'):
            self.pos = [14,1]
            board[14][1] = '&'
            filled[14][1] = 'troop'
        elif(called == 'k'):
            self.pos = [13,WIDTH_BASE - 2]
            board[13][WIDTH_BASE - 2] = '&'
            filled[13][WIDTH_BASE - 2] = 'troop'
        elif(called == 'l'):
            self.pos = [2,36]
            board[2][36] = '&'
            filled[2][36] = 'troop'
    
    def move(self, huts , cannons,list_buildings,all_walls,wizard_towers):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[self.pos[0]][self.pos[1]] = ' '
            dis = Inf
            for i in list_buildings:
                if i.health > 0:
                    for j in i.lists:
                        if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                            dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                            ind = i
                            indj = [i.pos_x + j[0],i.pos_y + j[1]]
            if dis != Inf:
                if(dis < self.range):
                    ind.health -= self.attack_power
                    # os.system('aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                    board[self.pos[0]][self.pos[1]] = '&'
                else:    
                    if(indj[0] < self.pos[0]):
                        self.pos[0] -= 1
                    elif(indj[0] > self.pos[0]):
                        self.pos[0] += 1
                    if (indj[1] < self.pos[1]):
                        self.pos[1] -= 1
                    elif(indj[1] > self.pos[1]):
                        self.pos[1] += 1
                    board[self.pos[0]][self.pos[1]] = '&'



# Change kar name
class Ballon(Troops):
    def __init__(self, called):
        super().__init__(called)
        self.health = HEALTH_LOON
        self.attack_power = ATTACK_POWER_LOON
        self.speed = SPEED_LOON
    def build(self,called):
        if(called == 'b'):
            self.pos = [24,1]
            board[24][1] = '^'
            filled[24][1] = 'troop'
        elif(called == 'm'):
            self.pos = [2,56]
            board[2][56] = '^'
            filled[2][56] = 'troop'
        elif(called == 'n'):
            self.pos = [23,WIDTH_BASE - 2]
            board[23][WIDTH_BASE - 2] = '^'
            filled[23][WIDTH_BASE - 2] = 'troop'
    
    def move(self, huts , cannons,list_buildings,all_walls,wizard_towers):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[self.pos[0]][self.pos[1]] = ' '
            dis = Inf
            for i in cannons:
                if i.health > 0:
                    for j in i.lists:
                        if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                            dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                            ind = i
                            indj = [i.pos_x + j[0],i.pos_y + j[1]]
            for i in wizard_towers:
                if i.health > 0:
                    for j in i.lists:
                        if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                            dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                            ind = i
                            indj = [i.pos_x + j[0],i.pos_y + j[1]]
            if dis == Inf:
                for i in list_buildings:
                    if i.health > 0:
                        for j in i.lists:
                            if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                                dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                                ind = i
                                indj = [i.pos_x + j[0],i.pos_y + j[1]]
            if dis != Inf:
                if(dis == 0):
                    ind.health -= self.attack_power
                    board[self.pos[0]][self.pos[1]] = '^'
                else:    
                    if(indj[0] < self.pos[0]):
                        self.pos[0] -= 1
                    elif(indj[0] > self.pos[0]):
                        self.pos[0] += 1
                    if (indj[1] < self.pos[1]):
                        self.pos[1] -= 1
                    elif(indj[1] > self.pos[1]):
                        self.pos[1] += 1
                    board[self.pos[0]][self.pos[1]] = '^'