# -*-coding: UTF-8-*-
import pygame
import random


class Tiro():
    def __init__(self, posX, posY):

        self.img = pygame.image.load("./shoot.png")
        self.X = posX + 40
        self.Y = posY

    def refreshPos(self):
        self.Y -= 3


class Meteoro():
    def __init__(self, posX, posY):

        self.imgMet = pygame.image.load("./meteoro.png")
        self.X = random.randint(1, 799)
        self.Y = 0

    def refreshPos(self):
        self.Y += 2


pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

tiros = []
meteoritos = []
fundo = pygame.image.load("./fundo1.jpg")
millenium = pygame.image.load("./millenium.png")
velocidade = 0
posX = 350
posY = 504
screen.blit(fundo, (0, 0))
screen.blit(millenium, (posX, posY))
tiro = None
meteorito = None

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        moveNave = pygame.key.get_pressed()
        if moveNave[pygame.K_SPACE]:
            tiros.append(Tiro(posX, posY))
        if moveNave[pygame.K_SPACE]:
            meteoritos.append(Meteoro(random.randint(1, 750), 0))

    moveNave = pygame.key.get_pressed()
    if moveNave[pygame.K_LEFT]:

        velocidade -= 0.3

        if velocidade < -3:
            velocidade = -3
        elif velocidade > 0:
            velocidade = 0

        posX += velocidade
        print('left')
        print(velocidade)

    elif moveNave[pygame.K_RIGHT]:
        velocidade += 0.3

        if velocidade > 3:
            velocidade = 3
        elif velocidade < 0:
            velocidade = 0

        posX += velocidade

    posX += velocidade

    if posX < 10:
        posX = 10
    elif posX > 690:
        posX = 690

    if velocidade > 0:
        velocidade -= 0.01

    if velocidade < 0:
        velocidade += 0.01

    screen.blit(fundo, (0, 0))

    for tiro in tiros:
        tiro.refreshPos()
        screen.blit(tiro.img, (tiro.X, tiro.Y))

    for meteorito in meteoritos:
        meteorito.refreshPos()
        screen.blit(meteorito.imgMet, (meteorito.X, meteorito.Y))

    screen.blit(millenium, (posX, posY))

    pygame.display.flip()
