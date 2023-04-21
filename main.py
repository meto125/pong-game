import os
import pygame
import random
import time
from math import fabs , sqrt
from ball import Ball
from stick import Stick

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)


class Board:
    def __init__(self,player1_score=0,player2_score=0):
        self.player1_score = player1_score
        self.player2_score = player2_score

class Screen:
    def __init__(self,width=900,height=600, color = BLACK):
        self.width = width
        self.height = height
        self.color = color
        


#setting the screen properties#####################################
main_screen = Screen()
win = pygame.display.set_mode((main_screen.width, main_screen.height))
pygame.display.set_caption("collisions")
img = pygame.image.load(r'C:\Users\ayman\pong-icon.png')
pygame.display.set_icon(img)
win.fill(main_screen.color)
#####################################################################

#setting the board properties#####################################
main_board = Board()
##################################################################

#setting player1 properties#####################################
player1 = Stick(main_screen.width-30, main_screen.height/2 - Stick(None,None).height/2)
################################################################

#setting player2 properties#####################################
player2 = Stick(30, main_screen.height/2 - Stick(None,None).height/2)
###############################################################

#setting ball properties#####################################
ball = Ball()
Ball()
#############################################################

while True:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit() 
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
            pygame.quit() 
            
    pygame.draw.circle(win, BLACK, (ball.xcor,ball.ycor), ball.radius)
    
    if ball.xcor+ball.radius >= main_screen.width:
        ball.x_vel*=-1
        #score+=1 ##################this part is wrong we still hadn't defined how we are going to print the score####################
        ball.xcor = main_screen.width/2
        ball.ycor = main_screen.height/2
        # ball.y_vel = random.uniform(-5, 5)
        # while fabs(ball.y_vel) < 1:
        #     ball.y_vel = random.uniform(-5, 5)
        # ball.x_vel = sqrt(fabs(ball.velocity**2 - ball.y_vel**2))
        ball.y_vel = ( fabs(ball.velocity) * ( (player2.ycor+player2.height/2) - ball.ycor) ) / sqrt( ( ((ball.xcor - ball.radius) - (player2.xcor + player2.width) ) ** 2) + ( ((ball.ycor ) - (player2.ycor + player2.height/2) ) ** 2) )
        ball.x_vel = -sqrt(fabs(ball.velocity**2 - ball.y_vel**2))
        
    if ball.xcor-ball.radius <= 0:
        ball.x_vel*=-1
        #score+=1 ##################this part is wrong we still hadn't defined how we are going to print the score####################
        ball.xcor = main_screen.width/2
        ball.ycor = main_screen.height/2
        # ball.y_vel = random.uniform(-5, 5)
        # while fabs(ball.y_vel) < 1:
        #     ball.y_vel = random.uniform(-5, 5)
        # ball.x_vel = sqrt(fabs(ball.velocity**2 - ball.y_vel**2))
        ball.y_vel = ( fabs(ball.velocity) * ( (player1.ycor+player1.height/2) - ball.ycor) ) / sqrt( ( ((ball.xcor + ball.radius) - (player1.xcor) ) ** 2) + ( ((ball.ycor ) - (player1.ycor + player1.height/2) ) ** 2) )
        ball.x_vel = sqrt(fabs(ball.velocity**2 - ball.y_vel**2))


        #print(score)##################this part is wrong we still hadn't defined how we are going to print the score####################
    if ball.ycor <= ball.radius or ball.ycor >= main_screen.height-ball.radius:
        # if test > 1 :
        #     test = 0
        if ball.ycor - ball.radius < 0:
            if ball.y_vel < 0:
                ball.y_vel*=-1 
        if ball.ycor + ball.radius > main_screen.height :
            if ball.y_vel > 0:
                ball.y_vel*=-1
    
    if ball.xcor + ball.radius >= player1.xcor and ball.ycor + ball.radius >= player1.ycor and ball.ycor - ball.radius <= player1.ycor + player1.height:
        # if test > 1 :
        #     test = 0  
        if ball.x_vel > 0:
            ball.x_vel *=-1
        space_from_cinter = ball.ycor-fabs(player1.ycor + player1.height/2)
        
        #print(score)##################this part is wrong we still hadn't defined how we are going to print the score####################
        
        ball.y_vel = space_from_cinter * (ball.max_y_vel / ( (player1.height+ball.radius) / 2) )
        ball.x_vel = -sqrt(fabs(ball.velocity**2 - ball.y_vel**2))
        
        # print("space from cinter: ", space_from_cinter)
        # print("ball.x_vel: " ,ball.x_vel )
        # print("ball.y_vel: ", ball.y_vel)
        
        
    if ball.xcor - ball.radius <= player2.xcor + player2.width and ball.ycor + ball.radius >= player2.ycor and ball.ycor - ball.radius <= player2.ycor + player2.height:
        # if test > 1 :
        #     test = 0  
        if ball.x_vel < 0:
            ball.x_vel *=-1
        space_from_cinter = ball.ycor-fabs(player2.ycor + player2.height/2)
        
        #print(score)##################this part is wrong we still hadn't defined how we are going to print the score####################
        
        ball.y_vel = space_from_cinter * (ball.max_y_vel / ( (player2.height+ball.radius) / 2) )
        ball.x_vel = sqrt(fabs(ball.velocity**2 - ball.y_vel**2))
        
        # print("space from cinter: ", space_from_cinter)
        # print("ball.x_vel: " ,ball.x_vel )
        # print("ball.y_vel: ", ball.y_vel)
            
            
            
        
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player1.ycor > 0:
        pygame.draw.rect(win, BLACK,(player1.xcor,player1.ycor,player1.width,player1.height))
        player1.ycor -= player1.velocity
    if key[pygame.K_DOWN] and player1.ycor < main_screen.height - player1.height:
        pygame.draw.rect(win, BLACK,(player1.xcor,player1.ycor,player1.width,player1.height))
        player1.ycor += player1.velocity
        
    if key[pygame.K_w] and player2.ycor > 0:
        pygame.draw.rect(win, BLACK,(player2.xcor,player2.ycor,player2.width,player2.height))
        player2.ycor -= player2.velocity
    if key[pygame.K_s] and player2.ycor < main_screen.height - player2.height:
        pygame.draw.rect(win, BLACK,(player2.xcor,player2.ycor,player2.width,player2.height))
        player2.ycor += player2.velocity
    
    ball.xcor+=ball.x_vel
    ball.ycor+=ball.y_vel
    
    pygame.draw.rect(win,player1.color,(player1.xcor,player1.ycor,player1.width,player1.height))
    pygame.draw.rect(win,player2.color,(player2.xcor,player2.ycor,player2.width,player2.height))
    pygame.draw.circle(win, ball.color, (ball.xcor,ball.ycor), ball.radius)
    pygame.display.update()