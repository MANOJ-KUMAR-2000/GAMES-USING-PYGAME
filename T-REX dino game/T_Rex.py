import pygame as pg
import random
import os

class Dino(object):
    death,jump,ideal = [pg.image.load(x)  for x in ['sprites/death.png','sprites/jump.png','sprites/ideal.png']]
    lows = [pg.image.load(x)  for x in ['sprites/low1.png','sprites/low2.png']]
    runs =  [pg.image.load(x)  for x in ['sprites/run1.png','sprites/run2.png']]
    
    def __init__(self, x,y,WINDOW, width, height):
        self.x = x
        self.y = y
        self.isjump = False
        self.islow = False
        self.jump_v = 10
        self.walkcount = 0
        self.jumpcount = 8
        self.WINDOW = WINDOW
        self.walk = 1
        self.hitbox = [self.x+5,self.y,40,45]
    def draw(self):
        self.hitbox = [self.x+5,self.y,30,45]
        
        if (not self.islow) and (not self.isjump):
            if self.walk >2:
                self.walk=0
            else:
                pass
            self.WINDOW.blit(self.runs[self.walk//2],(self.x,self.y))
            self.walk +=1
        if self.isjump:
            if self.jumpcount >= -8:
                neg = 1
                if self.jumpcount < 0:
                    neg = -1
                self.y -= (self.jumpcount **2) * 0.5* neg
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 8
            self.WINDOW.blit(Dino.jump, (self.x,self.y))
            
        if self.islow:
            self.hitbox = [self.x, self.y+10,50,35]
            if self.walk >2:
                self.walk=0
            else:
                pass
            self.WINDOW.blit(Dino.lows[self.walk//2],(self.x,self.y+10))
            self.walk +=1
            self.islow = False
        pg.display.update()
        
class Environment():
    stars = [pg.image.load(x)  for x in ['sprites/sun.png','sprites/moon.png']]
    cloud = pg.image.load('sprites/cloud.png')
    
    def __init__(self,WINDOW,width,height,cloud_pos):
        self.WINDOW = WINDOW
        self.width = width
        self.height = height
        self.star_x = width
        self.c_stars = 1
        self.cloud_x = cloud_pos[0]
        self.cloud_y = cloud_pos[1]
    def DrawStar(self):
        if self.star_x <=0:
            self.star_x = self.width
            self.c_stars += 1
        if self.c_stars >2:
            self.c_stars = 1
        self.WINDOW.blit(Environment.stars[self.c_stars//2], (self.star_x,self.height*0.1))
        self.star_x -= 1
        pg.display.update()
        
    def DrawCloud(self):
        if self.cloud_x <= 0:
            self.cloud_x = self.width
        self.WINDOW.blit(Environment.cloud, (self.cloud_x,self.cloud_y))
        self.cloud_x -= 2
        pg.display.update()


class Cactus():
    obstacles = [pg.image.load(x)  for x in ['sprites/CACTUS1.png', 'sprites/CACTUS2.png', 'sprites/CACTUS3.png'
                                            ,'sprites/CACTUS4.png', 'sprites/CACTUS5.png']]    
    L_obstacles = pg.image.load('sprites/obstacle-large.png')

    def __init__(self,WINDOW,width,height,pos):
        self.WINDOW = WINDOW
        self.width  = width
        self.height = height
        self.pos = pos
        self.cac_vel = 6
        self.c_cac = Cactus.obstacles[random.randrange(5)]
        self.hitbox = [pos[0],pos[1], 20,45]
    def draw(self):
        self.hitbox = [self.pos[0],self.pos[1], 18,45]
        if self.pos[0] <= 0:
            self.pos[0] = self.width
            self.c_cac = Cactus.obstacles[random.randrange(5)]
        self.WINDOW.blit(self.c_cac, self.pos)
        self.pos[0] = self.pos[0]-self.cac_vel    
        pg.display.update()
        
class Floor():
    floor1 = pg.image.load('sprites/floor.png')
    floor2 = pg.image.load('sprites/floor.png')
    
    def __init__(self,WINDOW,pos):
        self.WINDOW = WINDOW
        self.floor_x1 = 0
        self.floor_x2 = 500
        self.floor_y = pos
        self.floorvel = 6
   
    def DrawFloor(self):
        if self.floor_x1 <= -500:
            self.floor_x1 = 500
        if self.floor_x2 <= -500:
            self.floor_x2 = 500
        self.WINDOW.blit(Floor.floor1,(self.floor_x1,self.floor_y))
        self.WINDOW.blit(Floor.floor2,(self.floor_x2,self.floor_y))
        self.floor_x2 -= self.floorvel
        self.floor_x1 -= self.floorvel
        pg.display.update()
        
class Birds(object):
    birds = [pg.image.load(x)  for x in ['sprites/enemy1.png','sprites/enemy2.png']]
 
    def __init__(self,WINDOW, width, height, y_range):
        self.width = width
        self.height = height
        self.y_range = y_range
        self.bird_x = width
        self.bird_y = int(random.randrange(self.y_range[0],self.y_range[1]))
        self.WINDOW = WINDOW
        self.bird_vel = 7
        self.flycount = 1
        self.hitbox = [self.bird_x,self.bird_y, 30,20]
    def draw(self):
        self.hitbox = [self.bird_x,self.bird_y, 30,20]
        if self.flycount > 2:
            self.flycount = 0
        if self.bird_x<=0:
            self.bird_x = self.width*2
            self.bird_y =  int(random.randrange(self.y_range[0],self.y_range[1],4))
        self.WINDOW.blit(Birds.birds[self.flycount//2], (self.bird_x,self.bird_y))
        self.bird_x -= self.bird_vel

        self.flycount += 1
        pg.display.update()
    
