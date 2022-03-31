from distutils.command.build import build
from matplotlib.pyplot import fill
from .header import *
from .buildings import *
from .init2 import *
import time
def Queen_Special_Attack(self,direction,king_pos,all_troops,filled,board,cannons,wizard_towers,huts,town_hall,colr):
    building_geting_attacked = []
    for d in direction:
        if king_pos[0] + d[0] >= 0 and king_pos[0] + d[0] < HEIGHT_BASE and king_pos[1] + d[1] >= 0 and king_pos[1] + d[1] < WIDTH_BASE:
                colr[king_pos[0] + d[0]][king_pos[1] + d[1]] = "BLUE"
                if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                    if(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == '#'):
                        # town_hall.health -= self.attack_power
                        building_geting_attacked.append(town_hall)
                    elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][0])
                        # cannons[ind].health -= self.attack_power
                        building_geting_attacked.append(cannons[ind])
                    elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'Z'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][0])
                        # wizard_towers[ind].health -= self.attack_power
                        building_geting_attacked.append(wizard_towers[ind])
                    elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '_' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '/' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '\\' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '|'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][0])
                        # huts[ind].health -= self.attack_power
                        building_geting_attacked.append(huts[ind])
                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                        filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                        board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
    # Remove duplicates from building_geting_attacked
    building_geting_attacked = list(dict.fromkeys(building_geting_attacked))
    for i in building_geting_attacked:
        i.health -= self.attack_power
class King:
    """Class to build attackers."""

    def __init__(self, pos):
        """init2ializing class."""
        self.pos = pos
        self.health = HEALTH_KING
        self.speed = SPEED_KING
        self.attack_power = ATTACK_POWER_KING

    def build(self):
        """Building attackers."""
        if self.health > 0:
            board[self.pos[0]][self.pos[1]] = 'K'
            filled[self.pos[0]][self.pos[1]] = 'K'
        else:
            board[self.pos[0]][self.pos[1]] = 'D'
            filled[self.pos[0]][self.pos[1]] = ''

    def move(self, king_pos, huts, cannons,wizard_towers, called, all_troops):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[king_pos[0]][king_pos[1]] = ' '
            filled[king_pos[0]][king_pos[1]] = ''
            if called == 'a':
                if(filled[king_pos[0]][max(king_pos[1] - 1, 1)] == ''):
                    king_pos[1] = max(king_pos[1] - 1, 1)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
                    for i in wizard_towers:
                        i.attack(self,king_pos, all_troops)
            elif called == 'd':
                if(filled[king_pos[0]][min(king_pos[1] + 1, WIDTH_BASE - 2)] == ''):
                    king_pos[1] = min(king_pos[1] + 1, WIDTH_BASE - 2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
                    for i in wizard_towers:
                        i.attack(self,king_pos, all_troops)
            elif called == 'w':
                if(filled[max(king_pos[0] - 1, 1)][king_pos[1]] == ''):
                    king_pos[0] = max(king_pos[0] - 1, 2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
                    for i in wizard_towers:
                        i.attack(self,king_pos, all_troops)
            elif called == 's':
                if(filled[min(king_pos[0] + 1, HEIGHT_BASE-2)][king_pos[1]] == ''):
                    king_pos[0] = min(king_pos[0] + 1, HEIGHT_BASE-2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
                    for i in wizard_towers:
                        i.attack(self,king_pos, all_troops)

    def attack(self, town_hall, king_pos, huts, cannons,wizard_towers, called, all_troops,all_walls,last_direction,avatar):
        if avatar == "k":
            for i in cannons:
                i.attack(self, king_pos, all_troops)
            for i in wizard_towers:
                i.attack(self,king_pos, all_troops)
            direction =[]
            if called == ' ':
                direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for d in direction:
                    if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                        if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] == 'walls'):
                            for wl in all_walls:
                                if wl.pos_x == king_pos[0] + d[0] and wl.pos_y == king_pos[1] + d[1] and wl.health > 0:
                                    wl.health = 0
                                    wl.build()
                                    return
                        elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == '#'):
                            town_hall.health -= self.attack_power
                            os.system(
                                'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                            break
                        elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                            # cannon
                            ind = int(filled[king_pos[0] + d[0]]
                                        [king_pos[1] + d[1]][0])
                            cannons[ind].health -= self.attack_power
                            os.system(
                                'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                            break
                        elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'Z'):
                            # cannon
                            ind = int(filled[king_pos[0] + d[0]]
                                        [king_pos[1] + d[1]][0])
                            wizard_towers[ind].health -= self.attack_power
                            os.system(
                                'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                            break

                        elif(filled2[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'h'):
                            ind = int(filled[king_pos[0] + d[0]]
                                        [king_pos[1] + d[1]][0])
                            huts[ind].health -= self.attack_power
                            os.system(
                                'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                            break

                        elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                            filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                            board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
                            os.system(
                                'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                            break
            else:
                for i in range(5):
                    for j in range(5):
                        if i == 2 and j == 2:
                            continue
                        direction.append([i-2, j-2])
            building_geting_attacked = []
            for d in direction:
                if king_pos[0] + d[0] >= 0 and king_pos[0] + d[0] < HEIGHT_BASE and king_pos[1] + d[1] >= 0 and king_pos[1] + d[1] < WIDTH_BASE:
                        if called == ";":
                            colr[king_pos[0] + d[0]][king_pos[1] + d[1]] = "WHITE"
                        if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                            if(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == '#'):
                                # town_hall.health -= self.attack_power
                                building_geting_attacked.append(town_hall)
                            elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                                ind = int(filled[king_pos[0] + d[0]]
                                            [king_pos[1] + d[1]][0])
                                # cannons[ind].health -= self.attack_power
                                building_geting_attacked.append(cannons[ind])
                            elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'Z'):
                                ind = int(filled[king_pos[0] + d[0]]
                                            [king_pos[1] + d[1]][0])
                                # wizard_towers[ind].health -= self.attack_power
                                building_geting_attacked.append(wizard_towers[ind])
                            elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '_' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '/' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '\\' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '|'):
                                ind = int(filled[king_pos[0] + d[0]]
                                            [king_pos[1] + d[1]][0])
                                # huts[ind].health -= self.attack_power
                                building_geting_attacked.append(huts[ind])
                            elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                                filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                                board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
            # Remove duplicates from building_geting_attacked
            building_geting_attacked = list(dict.fromkeys(building_geting_attacked))
            for i in building_geting_attacked:
                i.health -= self.attack_power
        else:
            for i in cannons:
                i.attack(self, king_pos, all_troops)
            for i in wizard_towers:
                i.attack(self,king_pos, all_troops)
            if called == ' ':
                direction =[]
                positions=[]
                if last_direction == "w":
                    positions = [-8,0] 
                elif last_direction == "s":
                    positions = [8,0]
                elif last_direction == "a":
                    positions = [0,-8]
                elif last_direction == "d":
                    positions = [0,8]
                for i in range(5):
                        for j in range(5):
                            direction.append([positions[0]+i-2,positions[1]+j-2])
                building_geting_attacked = []
                for d in direction:
                    if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] == 'walls'):
                            for wl in all_walls:
                                if wl.pos_x == king_pos[0] + d[0] and wl.pos_y == king_pos[1] + d[1] and wl.health > 0:
                                    wl.health = 0
                                    wl.build()
                    if king_pos[0] + d[0] >= 0 and king_pos[0] + d[0] < HEIGHT_BASE and king_pos[1] + d[1] >= 0 and king_pos[1] + d[1] < WIDTH_BASE:
                            colr[king_pos[0] + d[0]][king_pos[1] + d[1]] = "BLUE"
                            if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                                if(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == '#'):
                                    # town_hall.health -= self.attack_power
                                    building_geting_attacked.append(town_hall)
                                elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                                    ind = int(filled[king_pos[0] + d[0]]
                                                [king_pos[1] + d[1]][0])
                                    # cannons[ind].health -= self.attack_power
                                    building_geting_attacked.append(cannons[ind])
                                elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'Z'):
                                    ind = int(filled[king_pos[0] + d[0]]
                                                [king_pos[1] + d[1]][0])
                                    # wizard_towers[ind].health -= self.attack_power
                                    building_geting_attacked.append(wizard_towers[ind])
                                elif(board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '_' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '/' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '\\' or board[king_pos[0] + d[0]][king_pos[1] + d[1]] == '|'):
                                    ind = int(filled[king_pos[0] + d[0]]
                                                [king_pos[1] + d[1]][0])
                                    # huts[ind].health -= self.attack_power
                                    building_geting_attacked.append(huts[ind])
                                elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                                    filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                                    board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
                # Remove duplicates from building_geting_attacked
                building_geting_attacked = list(dict.fromkeys(building_geting_attacked))
                for i in building_geting_attacked:
                    i.health -= self.attack_power
            else:
                direction =[]
                positions=[]
                if last_direction == "w":
                    positions = [-16,0] 
                elif last_direction == "s":
                    positions = [16,0]
                elif last_direction == "a":
                    positions = [0,-16]
                elif last_direction == "d":
                    positions = [0,16]
                for i in range(7):
                        for j in range(7):
                            direction.append([positions[0]+i-2,positions[1]+j-2])
                ATTACKTIME.clear()
                ATTACKTIME.append(time.time()+1)
                ATTACK_DATA.clear()
                for i in [self,direction,king_pos,all_troops,filled,board,cannons,wizard_towers,huts,town_hall,colr]:
                    ATTACK_DATA.append(i)
                # Queen_Special_Attack(ATTACKTIME,self,direction,king_pos,all_troops,filled,board,cannons,wizard_towers,huts,town_hall)
            