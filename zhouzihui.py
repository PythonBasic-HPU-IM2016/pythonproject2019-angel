import pygame
from pygame.locals import *

pygame.init()
#调用初始化函数
width,height=640,480
screen=pygame.display.set_mode((width,height))
#设置屏幕的长宽
keys=[False,False,False,False]
playerpos=[100,100]
pygame.mixer.init()

player=pygame.image.load("resources/images/dude.png")
grass=pygame.image.load("resources/images/grass.png")
castle=pygame.image.load("resources/images/castle.png")
#加载图片
hit=pygame.mixer.Sound("resources/audio/explode.wav")
enemy=pygame.mixer.Sound("resources/audio/enemy.wav")
shoot=pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)
while 1:
    screen.fill(0)
    #在给屏幕画任何东西之前用黑色进行填充
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    #这段代码首先是依次通过x进行循环。又是一个依次通过y的循环并且根据循环里x和y的值来画上草的效果。
    screen.blit(player,playerpos)
    #在屏幕的（100，100）坐标出添加所加载的兔子图片
    pygame.display.flip()
    #更新屏幕
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
            #检查一些新的事件，如果有退出命令，则终止程序的执行
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
                
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
            


