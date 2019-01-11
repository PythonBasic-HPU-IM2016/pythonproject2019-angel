import pygame
from pygame.locals import *
import math
import random 

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("game start")
keys = [False, False, False, False]
playerpos=[100,100]

#记录射出的箭头数，被击中的獾的数量
acc=[0,0]
#跟踪箭头
arrows=[]
#定义一个定时器，使得游戏里可以经过一段时间后就新建一只獾
badtimer=100
badtimer1=0
badguys=[[640,100]]
pygame.mixer.init()


player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
#加载獾图片
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

running = 1
exitcode = 0
while running:
    badtimer-=1

    screen.fill(0)
 

    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))





#玩家旋转兔子
    #获取鼠标的位置
    position = pygame.mouse.get_pos()
    #通过atan2函数得出的弧度值
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    #使玩家转向
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    #确定玩家的位置
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    #显示到屏幕上
    screen.blit(playerrot, playerpos1)



#画出箭头
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10#10是箭头的速度，单位移动的位移
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx#在玩家位置的基础上加入箭的位移
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        #循环把箭头画出来
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))


#画出獾    
    #检查badtime是否为0，如果为0，创建一个獾并重设badtime        
    if badtimer==0:
        #创建一个獾的初始位置
            badguys.append([640, random.randint(50,430)])
            #计时器不断减少
            badtimer=100-(badtimer1*2)
            #控制减少的时间
            if badtimer1>=35:
                badtimer1=35
            else:
                badtimer1+=5
    index=0
    for badguy in badguys:
        #獾进入城堡就消失
        if badguy[0]<-64:
            badguys.pop(index)
        #獾不断向前进    
        badguy[0]-=7
        index+=1
    #循环显示所有獾    
    for badguy in badguys:
        screen.blit(badguyimg, badguy)


    pygame.display.flip()
 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
              exit()

    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_w:
            keys[0]=True
        elif event.key==pygame.K_a:
            keys[1]=True
        elif event.key==pygame.K_s:
            keys[2]=True
        elif event.key==pygame.K_d:
            keys[3]=True
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            keys[0]=False
        elif event.key==pygame.K_a:
            keys[1]=False
        elif event.key==pygame.K_s:
            keys[2]=False
        elif event.key==pygame.K_d:
            keys[3]=False
#玩家移动按键
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
#跟踪箭头
    if event.type==pygame.MOUSEBUTTONDOWN:#检查是否点击了鼠标
        position=pygame.mouse.get_pos()#获取鼠标的位置
        acc[1]+=1#箭头数加一
        #向箭头的列表里加入箭头的选择角度，以及当前玩家的x,y坐标
        arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
 
 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
