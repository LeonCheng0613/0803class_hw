#開一個新的檔案，用rectangle控制烏龜和ghost，讓兩個以不同速度會不斷奔跑，感測烏龜碰到ghost就在螢幕上顯示紅色的驚嘆號，沒有感測就顯示黑色的mygame(如下圖)
import pygame
from sys import exit

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption('my game')

width = 800
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
title_font = pygame.font.Font('invasion2000.ttf', 50)
bg_surf = pygame.image.load('background.jpeg').convert_alpha()
player1_surf = pygame.image.load('leonardo.png').convert_alpha()
player2_surf = pygame.image.load('ghost.png').convert_alpha()

player1_rect = player1_surf.get_rect(midbottom = (80,398))
player2_rect = player2_surf.get_rect(midbottom = (200,398))
text_surf = title_font.render('My game', False, (0,0,0))
coll_surf = title_font.render('!!!', False, (255,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if player1_rect.left >= 800:
        player1_rect.left = 0
    else:
        player1_rect.left = player1_rect.left + 3
    if player2_rect.left >= 800:
        player2_rect.left = 0
    else:
        player2_rect.left = player2_rect.left + 7
    screen.blit(bg_surf, (0,0))
    screen.blit(player1_surf, player1_rect) 
    screen.blit(player2_surf, player2_rect)
    if player1_rect.colliderect(player2_rect):
        screen.blit(coll_surf, (100,150))
    else:
        screen.blit(text_surf, (100,150))
    pygame.display.update()
    clock.tick(60)