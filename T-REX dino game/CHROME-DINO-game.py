import pygame as pg
import random
import T_Rex as game
import time
import pickle

pg.init()

screen_w =640
screen_h = 360
WIN = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("CHROME DINO GAME")
restart = pg.image.load('sprites/restart.png')
ideal = pg.image.load('sprites/death.png')
sound = pg.mixer.Sound('musics/music.wav') 
GAME_OVER = False
game_close = False
dis = 0
hiscore = pickle.load(open('HIScore.txt',"rb"))
font = pg.font.SysFont("pixelmix",20)

dino = game.Dino(25,screen_h-70,WIN,screen_w,screen_h)
enemy1 = game.Birds(WIN, screen_w,screen_h, (dino.y-70,dino.y))
environment1 = game.Environment(WIN,screen_w,screen_h, (438,26))
environment2 = game.Environment(WIN,screen_w,screen_h, (200,95))
floor = game.Floor(WIN,dino.y+46)
cactus1 = game.Cactus(WIN,screen_w,screen_h, [231,dino.y+5])
cactus2 = game.Cactus(WIN,screen_w,screen_h, [594,dino.y+5])

clock = pg.time.Clock()

def check_hit(dino_box, bird_box, cactus_box):
    if dino_box[0]+dino_box[2] > cactus_box[0]:
        if dino_box[1]+dino_box[3]>cactus_box[1]:
            return True
    elif dino_box[0]+dino_box[3] > bird_box[0]:
        if dino_box[1] < bird_box[1]+bird_box[3]:
            return True
    else:
        return False
    
def DRAWINDOW():
    WIN.fill((255,255,255))
    if dis > 75:
        enemy1.draw()
    environment1.DrawStar()
    environment1.DrawCloud()
    environment2.DrawCloud()
    floor.DrawFloor()
    dino.draw()
    cactus1.draw()
    cactus2.draw()
    text1 = font.render(("score: " + str(int(dis))),5,(116,116,116))
    text2 = font.render("HI-SCORE "+str(hiscore),5,(116,116,116))
    WIN.blit(text1,(5,5))
    WIN.blit(text2,(5,25))
    pg.display.update()

while not GAME_OVER:
    if dis%100==0 and dis>100:
        floor.floorvel += 1
        cactus1.cac_vel += 1
        cactus2.cac_vel +=1
    dis += 0.25
    clock.tick(20)

    while game_close:
        if hiscore < dis:
            hiscore = dis
            pickle.dump(hiscore,open('HIScore.txt',"wb"))   
        t = font.render("TAP SPACE TO RUN",5,(0,0,0))
        WIN.blit(t,(screen_w//2-55, screen_h//2-35))
        WIN.blit(restart, (screen_w//2-10, screen_h//2-10))
        cactus1.pos = [340,floor.floor_y-40]
        cactus2.pos = [750,floor.floor_y-40]    
        enemy1.bird_x = 724
        enemy1.hitbox = [enemy1.bird_x,enemy1.bird_y, 30,20]
        dis=0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_close = False
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:                  
                    game_close = False
                    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME_OVER = True
            
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] or keys[pg.K_SPACE]:
        sound.play()
        dino.isjump = True
    if not dino.isjump:
        if keys[pg.K_DOWN]:
            dino.islow = True
            
    DRAWINDOW()
    
    if check_hit(dino.hitbox, enemy1.hitbox, cactus1.hitbox) or check_hit(dino.hitbox, enemy1.hitbox, cactus2.hitbox):
        WIN.blit(ideal, (dino.x, dino.y))
        game_close = True
        
pg.quit()
