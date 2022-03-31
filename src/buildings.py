from matplotlib.pyplot import fill
from .header import *
# from .init2 import *
import os
class Buildings:
    # TOTAL_BUILDING = 0
    """Class to build buildings."""
    def __init__(self, name, pos_x, pos_y, lists,ind):
        """init2ializing class."""
        # Buildings.TOTAL_BUILDING += 1
        self.name = name
        # Starting Position of the building (top left corner)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lists = lists
        self.health = 100
        self.ind = ind
        self.power_on = False
        if self.name[0] == 'T':
            self.health = HEALTH_TOWN
        elif self.name[0] == "h":
            self.health = HEALTH_HUT
        elif self.name[0] == "c":
            self.health = HEALTH_CANNON
        elif self.name == "wt":
            self.health = HEALTH_WT

    def build(self):
        """Building buildings."""
        if(self.health > 0):
            for i in self.lists:
                board[self.pos_x + i[0]][self.pos_y + i[1]] = i[2]
                filled[self.pos_x + i[0]][self.pos_y + i[1]] = str(self.ind)
                filled2[self.pos_x + i[0]][self.pos_y + i[1]] = self.name
        else:
            # if filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != '' and filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != 'K' and filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != '*':
                # Buildings.TOTAL_BUILDING -= 1
            for i in self.lists:
                board[self.pos_x + i[0]][self.pos_y + i[1]] = ' '
                filled[self.pos_x + i[0]][self.pos_y + i[1]] = ''

class Cannon(Buildings):
    
    def attack(self,king,king_pos,all_troops):
        """Attacking Troops/King."""
        self.range = RANGE_CANNON
        self.attack_power = ATTACK_POWER_CANNON
        if self.health <= 0:
            self.power_on = False
        elif abs(self.pos_x - king_pos[0]) + abs(self.pos_y - king_pos[1]) <= self.range and king.health > 0:
            king.health -= self.attack_power
            # os.system('aplay -q ./sounds/cannon_shot.wav& 2>/dev/null')
            if king.health <= 0:
                king.health = 0
                board[king_pos[0]][king_pos[1]] = 'D'
                filled[king_pos[0]][king_pos[1]] = ''
                self.power_on = False
            else:
                self.power_on = True
        else:
            self.power_on = False
            for i in all_troops:
                if board[i.pos[0]][i.pos[1]] == '^':
                    continue
                if abs(self.pos_x - i.pos[0]) + abs(self.pos_y - i.pos[1]) <= self.range and i.health > 0:
                    # os.system('aplay -q ./sounds/cannon_shot.wav& 2>/dev/null')
                    i.health -= self.attack_power
                    if i.health <= 0:
                        board[i.pos[0]][i.pos[1]] = ' '
                        filled[i.pos[0]][i.pos[1]] = ''
                        all_troops.remove(i)
                    self.power_on = True
                    break

class Walls(Buildings):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 1
        
    def build(self):
        if self.health > 0:
            board[self.pos_x][self.pos_y] = 'W'
            filled[self.pos_x][self.pos_y] = 'walls'
        else:
            if board[self.pos_x][self.pos_y] == 'W':
                board[self.pos_x][self.pos_y] = ' '
                filled[self.pos_x][self.pos_y] = ''

class Wizard_Tower(Buildings):
    def attack(self,king,king_pos,all_troops):
        """Attacking Troops/King."""
        self.range = RANGE_WT
        self.attack_power = ATTACK_POWER_WT
        if self.health <= 0:
            self.power_on = False
        elif abs(self.pos_x - king_pos[0]) + abs(self.pos_y - king_pos[1]) <= self.range and king.health > 0:
            king.health -= self.attack_power
            for i in range(-1,2):
                for j in range(-1,2):
                    colr[king_pos[0]+i][king_pos[1]+j] = "WIZARD_TOWER"
                    if i == 0 and j == 0:
                        continue
                    else:
                        if board[king_pos[0]+i][king_pos[1]+j] == '^' or board[king_pos[0]+i][king_pos[1]+j] == '&' or board[king_pos[0]+i][king_pos[1]+j] == '*':
                            for trp in all_troops:
                                if trp.pos[0] == king_pos[0]+i and trp.pos[1] == king_pos[1]+j:
                                    trp.health -= self.attack_power
                                    if trp.health <= 0:
                                        board[trp.pos[0]][trp.pos[1]] = ' '
                                        filled[trp.pos[0]][trp.pos[1]] = ''
                                        all_troops.remove(trp)

            if king.health <= 0:
                king.health = 0
                board[king_pos[0]][king_pos[1]] = 'D'
                filled[king_pos[0]][king_pos[1]] = ''
                self.power_on = False
            else:
                self.power_on = True
        else:
            self.power_on = False
            for i in all_troops:
                if abs(self.pos_x - i.pos[0]) + abs(self.pos_y - i.pos[1]) <= self.range and i.health > 0:
                    # os.system('aplay -q ./sounds/cannon_shot.wav& 2>/dev/null')
                    i.health -= self.attack_power
                    if i.health <= 0:
                        board[i.pos[0]][i.pos[1]] = ' '
                        filled[i.pos[0]][i.pos[1]] = ''
                        all_troops.remove(i)
                    for x in range(-1,2):
                        for y in range(-1,2):
                            colr[i.pos[0]+x][i.pos[1]+y] = "WIZARD_TOWER"
                            if x == 0 and y == 0:
                                continue
                            else:
                                if board[i.pos[0]+x][i.pos[1]+y] == '^' or board[i.pos[0]+x][i.pos[1]+y] == '&' or board[i.pos[0]+x][i.pos[1]+y] == '*' or board[i.pos[0]+x][i.pos[1]+y] == 'K':
                                    if board[i.pos[0]+x][i.pos[1]+y] == 'K':
                                        king.health -= self.attack_power
                                        if king.health <= 0:
                                            king.health = 0
                                            board[king_pos[0]][king_pos[1]] = 'D'
                                            filled[king_pos[0]][king_pos[1]] = ''
                                    for trp in all_troops:
                                        if trp.pos[0] == i.pos[0]+x and trp.pos[1] == i.pos[1]+y:
                                            trp.health -= self.attack_power
                                            if trp.health <= 0:
                                                board[trp.pos[0]][trp.pos[1]] = ' '
                                                filled[trp.pos[0]][trp.pos[1]] = ''
                                                all_troops.remove(trp)
                    self.power_on = True
                    break