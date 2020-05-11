"""
author : MANOJ KUMAR S
date   : 11.05.2020

"""
import pygame as pg  # importing pygame packages as pg
import time
import random

# --------------------SIMPLE BASIC SNAKE GAME--------------------------- #


def draw_snake_length(snake_list):
    # it is to draw the body of the snake
    for i in snake_list:
        pg.draw.rect(dis, (0, 0, 0), [i[0], i[1], block_size, block_size])
        pg.display.update()


def lives(n):
    text = font.render("LIVES:" + str(n), True, (255, 180, 50))
    dis.blit(text, [700, 0])
    pg.display.update()


def food():
    # it is to show the food at random position
    food_x = round(random.randrange(1, width - vel) / 10) * 10
    food_y = round(random.randrange(1, height - vel) / 10) * 10
    return food_x, food_y
    # returns the co-ordinates of the food


def score(scores, pos):  # shows the score of the player

    text = font.render(scores, True, (255, 200, 100))
    dis.blit(text, pos)
    pg.display.update()


def msg(message):
    # shows the message when game over
    font1 = pg.font.SysFont('comicans', 50)
    text = font1.render(message, 1, (255, 10, 0))
    dis.blit(text, [(width // 2) - (text.get_width() // 2), height // 2])
    pg.display.update()


# width and height of a gaming window
width = 800
height = 600

pg.init()  # intializing a pygame
dis = pg.display.set_mode((width, height))  # setting a display size
pg.display.set_caption("SNAKE GAME", "snake_icon.ico")

music = pg.mixer.music.load('bgmusic.mp3')
pg.mixer.music.play(-1)   # music will play till we close window

white = (255, 255, 255)  # declaring a white color
black = (0, 0, 0)  # declaring a black color

x, y = 200, 100  # assigning a snake head co-ordinates

x1, y1 = 0, 0  # assigning a change in position co-ordinates
vel = 10  # velocity of snake
block_size = 10  # size of a snake

# variable declarations
length_of_snake = 1
life = 3
snake_len_list = []
clock = pg.time.Clock()
font = pg.font.SysFont('comicans', 35)
food_pos = food()

game_over = False
game_close = False

while not game_over:  # it is the main loop of the game
    # when the game_over became True the main loop terminates and game ends
    while game_close:
        # here it asks the player wheather to quit or tryagain when they loses
        dis.fill((0, 0, 255))
        score("SCORE:" + str(length_of_snake - 1), [320, 50])
        msg("Q - quit  R - tryagain")
        pg.display.update()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                game_over = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:  # it is a letter Q on keyboard
                    game_over = True
                    game_close = False

                if event.key == pg.K_r:  # it is letter R on keyboard
                    # incase player need to try again
                    game_close = False
                    x = 200  # everything begins from beginning values
                    y = 100
                    length_of_snake = 1
                    snake_len_list = []
                    life = 3
                    food_pos = food()
    for event in pg.event.get():

        if event.type == pg.QUIT:
            game_over = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:  # moves the snake left with velocity vel
                x1 = -vel  # -ve indicate's to move in opposite direction
                y1 = 0

            if event.key == pg.K_RIGHT:
                x1 = vel
                y1 = 0

            if event.key == pg.K_UP:
                y1 = -vel
                x1 = 0

            if event.key == pg.K_DOWN:
                y1 = vel
                x1 = 0

    x += x1
    y += y1

    if x >= width or x < 0 or y < 0 or y >= height:
        life -= 1
        x, y = 200, 100
        score("life-1", [350, 300])  # to print the life decrement when hit
        time.sleep(2)
    dis.fill(white)

    if x == food_pos[0] and y == food_pos[1]:
        food_pos = food()  # here it checks wheather snake eats food or not
        length_of_snake += 1

    pg.draw.rect(dis, (255, 0, 0), [food_pos[0], food_pos[1], block_size, block_size])
    # food is a red cube
    # snake is in black
    snake_head = [x, y]
    snake_len_list.append(snake_head)

    if len(snake_len_list) > length_of_snake:
        del snake_len_list[0]

    for j in snake_len_list[:-1]:
        if j == snake_head:  # it is to check the snake body collision
            life -= 1
            score("life-1", [350, 300])  # to print the life decrement when hit
            x, y = 200, 100  # re-positioning the (x, y) co-ordinates after hitting
            time.sleep(2)

    if life <= 0:    # game end's when life is 0
        game_close = True

    draw_snake_length(snake_len_list)
    score("SCORE:" + str(length_of_snake - 1), [0, 0])  # always display's the score
    lives(life)  # printing the score in game window
    pg.display.update()
    clock.tick(30)

pg.quit()  # pygame quits
