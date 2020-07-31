import pygame
import time
import random

pygame.init()

width=300
length=300

dis=pygame.display.set_mode((width,length))
pygame.display.update()

pygame.display.set_caption('SNAKE GAME')

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,102)

clock=pygame.time.Clock()
snake_block=10
food_size=10
snake_speed=20

font_style=pygame.font.SysFont('bahnschrift',15)
score_font=pygame.font.SysFont('comicsansms',20)

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green,[x[0],x[1],snake_block,snake_block])

def my_score(score):
    value=score_font.render('YOUR SCORE: '+str(score),True,yellow)
    dis.blit(value,[0,0])

def message(msg, color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[20,length/3])

def playagain():
    game_over=False
    game_quit=False
    
    x1=width/2
    y1=length/2

    dx1=0
    dy1=0

    snake_list=[]
    snake_len=1

    x2=round(random.randrange(0,width-snake_block)/10.0)*10.0
    y2=round(random.randrange(0,length-snake_block)/10.0)*10.0

    while not game_over:
        while game_quit==True:
            dis.fill(blue)
            message('YOU LOST!!PRESS P-PLAY AGAIN OR Q-QUIT',green)
            my_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event .get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_quit=False
                    if event.key==pygame.K_p:
                        playagain()
                        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    dx1=-snake_block/2
                    dy1=0    
                elif event.key==pygame.K_RIGHT:
                    dx1=snake_block/2
                    dy1=0             
                elif event.key==pygame.K_UP:
                    dy1=-snake_block/2
                    dx1=0 
                elif event.key==pygame.K_DOWN:
                    dy1=snake_block/2
                    dx1=0
            if x1>=width or x1<=0 or y1>=length or y1<=0:
                game_quit=True
                
            x1+=dx1
            y1+=dy1
            dis.fill(black)
            pygame.draw.rect(dis,green,[x1,y1,snake_block,snake_block])
            snake_head=[]
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list)>snake_len:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x==snake_head:
                    game_quit=True

            my_snake(snake_block, snake_list)
            my_score(snake_len-1)
            
            pygame.draw.rect(dis,red,[x2,y2,food_size,food_size])
            pygame.display.update()

            if x1==x2 and y1==y2:
                x2=round(random.randrange(0,width-snake_block)/10.0)*10.0
                y2=round(random.randrange(0,length-snake_block)/10.0)*10.0
                snake_len+=1

            clock.tick(snake_speed)
        
    message('YOU LOST',white)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

playagain()
