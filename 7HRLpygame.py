from numpy import linalg as math
import numpy as np

import random
import sys

import pygame

clock = pygame.time.Clock()

screen = {}

class Display:
    def __init__(self,player,enemy,walls):
        self.done = False
        self.Enemies = enemy
        self.Player = player
        self.Font = pygame.font.SysFont('Arial', 25) #pygame.font.Font(None, 25)
        self.Walls = walls

    def UpdateStatus(self):
        print "UpdateStatus"
        texts = self.Font.render(str(self.Player.health)+"jhdakljhdskajhsdkjahsdkljahfdkljdshluwehkrjhqwkfb", 0,(255,0,255))
        rect = texts.get_rect()
        print rect
        screen.blit(texts,(0,0))

    def displayLoop(self):
        while not self.done:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE):
                        self.done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: self.Player.ypos -= 3
            if pressed[pygame.K_DOWN]: self.Player.ypos += 3
            if pressed[pygame.K_LEFT]: self.Player.xpos -= 3
            if pressed[pygame.K_RIGHT]: self.Player.xpos += 3
            #if pressed[pygame.K_ESCAPE]: self.done = True

            screen.fill((0, 0, 255))
            self.Walls.Draw()
            self.Enemies.Draw()
            self.Player.Draw()
            pygame.display.update()
            #self.UpdateStatus()
            clock.tick(60)

            print self.Player.xpos
            print self.Player.ypos

        pygame.quit()
        quit()

class Walls:
    def __init__(self,numWalls,sizex,sizey,color):
        self.numWalls = numWalls
        self.color = color
        self.size = 16
        self.Walls = [[False]*(sizex/self.size) for i in range(sizey/self.size)]
        self.genWalls(sizex,sizey)
        print self.Walls
        print len(self.Walls)
        print len(self.Walls[0])
        #print self.Walls
        #self.Walls = [Room(r,sizex,sizey) for r in range(numRooms)]

    def Draw(self):
        for column in range(len(self.Walls)):
            for row in range(len(self.Walls[0])):
                if self.Walls[column][row]:
                    pygame.draw.rect(screen, self.color, pygame.Rect(self.size*column, self.size*row, self.size, self.size))

    def genWalls(self,sizex,sizey):
        sizex = sizex/self.size
        sizey = sizey/self.size
        for n in range(self.numWalls):
            print n
            xpos = np.random.randint(0,sizex)
            ypos = np.random.randint(0,sizey)
            self.Walls[xpos][ypos] = True

class Wall:
    def __init__(self,rID,sizex,sizey):
        self.rID = rID
        self.xpos = np.random.randint(16,960/sizex)*16
        self.ypos = np.random.randint(16,960/sizey)*16
        offest1 = 35
        offset2 = 33
        self.sizex = sizex#np.random.randint(abs(sizex-offest1),abs(sizex+offset2))
        self.sizey = sizey#np.random.randint(abs(sizey-offest1),abs(sizey+offset2))
        #self.items = Items(numItems)

#class Items
#    def __init__(self,numItems):
#        self.numItems = numItems
#        self.Items = [Item(i,np.random.randint(, )) for i in range(numItems)]
#class Item
#    def __init__(self,iID,xpos,ypos,sizex,sizey):

class Enemies:
    def __init__(self,numEnemy,walls):
        self.enemy = []
        self.indexwalls = [np.where(walls[i])[0] for i in range(len(walls))]
        print self.indexwalls
        for i in range(numEnemy):
            temp = np.random.randint(0,50)
            self.enemy.append(Enemy(self.indexwalls[temp][0],temp,(125,34,24),12))

    def Update(self):
        for e in self.enemy:
            e.xpos

    def Draw(self):
        for e in self.enemy:
            pygame.draw.rect(screen, e.color, pygame.Rect(e.xpos*e.size,e.ypos*e.size, e.size, e.size))

'''
class Astar:
    def __init__(self,start,goal,enemy,walls):
        self.enemy=enemy
        self.walls = walls
        self.start = start
        self.goal = goal
        self.open_list = []
        self.cloased_list =[]

    def heuristic(self,start,goal):
        return abs(start.x-goal.x) + abs(start.y-goal.y)

    def Astar(start, goal)
        open_list = start
        closed_list = []
        startg = 0
        startf = startg + self.heuristic(start, goal)
        while is_empty(open_list):
            current = open_list element with lowest f cost
            if current = goal:
                return construct_path(goal)
            remove current from open_list
            closed_list.append(current)
            for neighbor in neighbors(current)
                if neighbor not in closed_list
                    neighbor.f = neighbor.g + heuristic(neighbor, goal)
                if neighbor is not in open_list
                    add neighbor to open_list
                else
                    openneighbor = neighbor in open_list
                    if neighbor.g < openneighbor.g
                        openneighbor.g = neighbor.g
                        openneighbor.parent = neighbor.parent
            return False // no path exists

function neighbors(node)
  neighbors = set of valid neighbors to node // check for obstacles here
  for each neighbor in neighbors
    if neighbor is diagonal
      neighbor.g = node.g + diagonal_cost // eg. 1.414 (pythagoras)
    else
      neighbor.g = node.g + normal_cost // eg. 1
    neighbor.parent = node
  return neighbors

function construct_path(node)
  path = set containing node
  while node.parent exists
    node = node.parent
    add node to path
  return path
'''

class Enemy:
    def __init__(self,newxpos,newypos,color,mtype):
        self.xpos = newxpos
        self.ypos = newypos
        self.mtype = mtype
        self.size = 16
        self.color = color
        #pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.size, self.size))

class Player:
    def __init__(self,size,newxpos,newypos):
        self.xpos = newxpos
        self.ypos = newypos
        self.size = size
        self.health = 100
        self.stats = ""
        self.color = (0,255,0)

    def Draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.size, self.size))

def main():
    print "Hello"
    #while not done

if __name__ == "__main__":

    sizex = sizey = 800
    pygame.init()
    #pygame.font.init()
    pygame.display.set_caption('7HRL 2018')
    screen = pygame.display.set_mode((sizex, sizey))
    p = Player(16,0,0)
    w = Walls(300,sizex,sizey,(0,0,0))
    e = Enemies(15,w.Walls)
    disp = Display(p,e,w)

    disp.displayLoop()
