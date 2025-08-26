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

b_g =pygame.image.load("bg (2).png")

pygame.display.set_caption("Space Invader")

play_img = pygame.image.load("spaceship (1).png")
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

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(b_g,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
             playx_ch = -5  
            if event.key == pygame.K_RIGHT:
             playx_ch = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
             bulletx = playx
            fire_bullet(bulletx , bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT , pygame.K_RIGHT]:
             playx_ch = 0

        playx += playx_ch
        playx = max(0 , min(playx , s_w - 64))

        for i in range (num_of_ene):
           if eney[i] > 340:
               for j in range(num_of_ene):
                 eney[j] = 2000
               game_over_text()
               break
           enex[i] += enex_ch[i]
           if enex[i] <= 0 or enex[i] >= s_w - 64:
             enex_ch[i] *= -1
             eney[i] += eney_ch[i]

           if isCollision(enex[i],eney[i],bulletx,bullety):
              bullety = play_s_y
              bullet_state = "ready"
              score_val += 1
              enex[i] = random.randint(0,s_w - 64)
              eney[i] = random.randint(ene_s_y_min,ene_s_y_max)
           enemy(enex[i], eney[i],i)

        if bullety <= 0:
           bullety = play_s_y
           bullet_state = "ready"
        elif bullet_state == "fire":
           fire_bullet(bulletx , bullety)
           bullety -=bullety_ch

        player(playx,playy)
        show_score(textx,texty)
        pygame.display.update()
                                       
              
            
        
                

