import math
import random
import pygame

s_w = 800
s_h = 500
play_s_x = 370
play_s_y = 380
ene_s_y_min = 50
ene_s_y_max = 150
ene_sp_x = 4
ene_sp_y = 40
bullet_sp_y = 10
collision_d = 27

pygame.init()

screen = pygame.display.set_mode((s_w , s_h))

b_g =pygame.image.load("background.png")

pygame.display.set_caption("Space Invader")

play_img = pygame.image.load("player.png")
playx = play_s_x
playy = play_s_y
playx_ch = 0

ene_img = []
enex = []
eney = []
enex_ch = []
eney_ch = []
num_of_ene = 6

for i in range(num_of_ene):
    ene_img.append(pygame.image.load("enemy.png"))
    enex.append(random.randint(0,s_w - 64))
    eney.append(random.randint(ene_s_y_min , ene_s_y_max))
    enex_ch.append(ene_sp_x)
    eney_ch.append(ene_sp_y)

bulleting = pygame.image.load("bullet.png")
bulletx = 0
bullety = play_s_y
bulletx_ch = 0
bullety_ch = bullet_sp_y
bullet_state = "ready"

score_val = 0
font = pygame.font.Font ( "freesansbold.ttf",32)
textx = 10
texty = 10
over_font = pygame.font.Font ( "freesansbold.ttf",64)

def show_score(x,y):
    score = font.render("Score :" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(play_img, (x,y))

def enemy(x,y,i):
    screen.blit(ene_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulleting, (x + 16 , y + 10))

def isCollision ( enex , eney , bulletx , bullety):
    d = math.sqrt((enex - bulletx) ** 2 + (eney - bullety) ** 2)
    return d < collision_d
                

