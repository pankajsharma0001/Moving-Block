import pygame
import random
import time

pygame.init()

width = 800
height = 600
block = 20

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Block Game - Pankaj Sharma")

clock = pygame.time.Clock()

def show_pause_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("PAUSED", True, 'black')
    text_rect = text.get_rect(center=(width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.update()


def score():
    font = pygame.font.SysFont('Arial', 20)
    text = font.render('Score:'+ str(count), True, 'black')
    screen.blit(text, (0, 0))

def game_over(  ):
    font = pygame.font.SysFont('Arial', 25, 'bold')
    text = font.render('Your Score is : '+ str(count), True, 'black')
    screen.blit(text, (width / 2 - 50, height / 2))
    pygame.display.update()
    time.sleep(2)
    start_game()


def instruction():
    screen.fill(white)
    font = pygame.font.SysFont('Arial', 20)
    text = 'How to play Game?\n Left & Right = A & D \n Pause = Space \n Quite = Escape'
    lines = text.split('\n')
    text_surfaces =  []

    for line in lines:
        text_surfaces.append(font.render(line, True, (0, 0, 0)))

    for i, surface in enumerate(text_surfaces):
        screen.blit(surface, (50, 50 + (i * 30)))

    pygame.display.update()
    time.sleep(3)
    start_game()


def start_game():
    global count
    x_enemy = random.randint(0, width-50)
    y_enemy = 0
    x = width / 2
    y = height - block
    x_change = 0
    count = 0
    fps = 60
    running = True
    paused = False
    while running:
        rect_enemy = pygame.Rect(x_enemy, y_enemy, 50, 50)
        rect_player = pygame.Rect(x, y, block, block)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_a:
                    x_change = -10
                if event.key == pygame.K_d:
                    x_change = 10
                if event.key == pygame.K_SPACE:
                    paused = not paused
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        if paused:
            show_pause_screen()

        else:
            screen.fill(white)
            score()
            pygame.draw.rect(screen, red, rect_enemy)
            pygame.draw.rect(screen, blue, rect_player)

            collide = pygame.Rect.colliderect(rect_player, rect_enemy)

            if collide:
                running = False
                game_over()

            y_enemy += 10

            if rect_enemy.bottom >= height:
                x_enemy = random.randint(0, width - 50)
                y_enemy = 0
                count += 1
                fps += 0.5
            if x < 0:
                x = 1
                x_change=0
            if x > width:
                x = width-25
                x_change = 0

            x = x + x_change
            pygame.display.update()
            clock.tick(fps)

instruction()
pygame.quit()