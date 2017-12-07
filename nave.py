# -*-coding: UTF-8-*-
import pygame
import random


class Nave():
    def __init__(self):

        self.img = pygame.image.load("./millenium.png")
        self.velocidade = 0
        self.velocidadeY = 0
        self.posX = 580
        self.posY = 700
        self.Rect = pygame.Rect(self.posX, self.posY, 100, 96)
        self.vida = 20
        self.pontos = 0

    def moveNave(self):
            moveNave = pygame.key.get_pressed()
            if moveNave[pygame.K_LEFT]:

                self.velocidade -= 1

                if self.velocidade < -7:
                    self.velocidade = -7
                elif self.velocidade > 0:
                    self.velocidade = 0

                self.posX += self.velocidade

            elif moveNave[pygame.K_RIGHT]:
                self.velocidade += 1

                if self.velocidade > 7:
                    self.velocidade = 7
                elif self.velocidade < 0:
                    self.velocidade = 0

                self.posX += self.velocidade

            self.posX += self.velocidade

            if self.posX < 10:
                self.posX = 10
            elif self.posX > 1090:
                self.posX = 1090

            if self.velocidade > 0:
                self.velocidade -= 0.5

            if self.velocidade < 0:
                self.velocidade += 0.5

            if moveNave[pygame.K_UP]:

                self.velocidadeY -= 1

                if self.velocidadeY < -7:
                    self.velocidadeY = -7
                elif self.velocidadeY > 0:
                    self.velocidadeY = 0

                self.posY += self.velocidadeY

            elif moveNave[pygame.K_DOWN]:
                self.velocidadeY += 1

                if self.velocidadeY > 7:
                    self.velocidadeY = 7
                elif self.velocidadeY < 0:
                    self.velocidadeY = 0

                self.posY += self.velocidadeY

            self.posY += self.velocidadeY

            if self.posY < 10:
                self.posY = 10
            elif self.posY > 700:
                self.posY = 700

            if self.velocidadeY > 0:
                self.velocidadeY -= 0.5

            if self.velocidadeY < 0:
                self.velocidadeY += 0.5

            self.Rect = pygame.Rect(self.posX, self.posY, 100, 96)


class Tiro():
    def __init__(self, posX, posY):

        self.img = pygame.image.load("./shoot.png")
        self.posX = posX + 40
        self.posY = posY
        self.Rect = pygame.Rect(self.posX, self.posY, 30, 15)

    def refreshPos(self):
        self.posY -= 20
        self.Rect = pygame.Rect(self.posX, self.posY, 30, 15)


class Meteoro():
    def __init__(self, posX, screen):

        self.img = pygame.image.load("./meteoro.png")
        self.posX = posX
        self.posY = -200
        self.Rect = pygame.Rect(self.posX, self.posY, 50, 50)
        self.vida = random.randint(1, 5)*2
        self.size = self.vida/2
        self.rotate = random.randint(-3, 3)
        self.angulo = 0
        self.screen = screen
        self.velo = random.randint(2, 8)

    def refreshPos(self):
        self.posY += self.velo
        self.angulo += self.rotate

    def Carimbo(self):
        tamw = self.img.get_rect().width
        tamh = self.img.get_rect().height
        img = pygame.transform.scale(self.img, (self.size*tamw, self.size*tamh))
        img = pygame.transform.rotate(img, self.angulo)
        self.screen.blit(img, (self.posX, self.posY))
        self.Rect = pygame.Rect(self.posX, self.posY, self.size*tamw, self.size*tamh)


pygame.init()

font = pygame.font.SysFont(None, 60, bold=False, italic=False)
screen = pygame.display.set_mode((1200, 800), 0, 32)

tiros = []
meteoritos = []
fundo = pygame.image.load("./fundo1.jpg")
millenium = Nave()
tiro = None
meteorito = None
clock = pygame.time.Clock()

while True:
    clock.tick(30)

    screen.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        moveNave = pygame.key.get_pressed()
        if moveNave[pygame.K_SPACE]:
            tiros.append(Tiro(millenium.posX, millenium.posY))

    met = random.randint(0, 1000)
    if met > 980:
        meteoritos.append(Meteoro(random.randint(1, 1120), screen))

    millenium.moveNave()

    for tiro in tiros:
        tiro.refreshPos()
        screen.blit(tiro.img, (tiro.posX, tiro.posY))
        if tiro.posY < -40:
            tiros.remove(tiro)

    for meteorito in meteoritos:
        meteorito.refreshPos()
        meteorito.Carimbo()
        if meteorito.posY > 800:
            meteoritos.remove(meteorito)
        if meteorito.Rect.colliderect(millenium.Rect):
            meteoritos.remove(meteorito)
            millenium.vida -= 1
            if millenium.vida == 0:
                exit()

    for meteorito in meteoritos:
        for tiro in tiros:
            if meteorito.Rect.colliderect(tiro.Rect):
                tiros.remove(tiro)
                meteorito.vida -= 1
                if meteorito.vida == 0:
                    meteoritos.remove(meteorito)
                    millenium.pontos += 1

    screen.blit(millenium.img, (millenium.posX, millenium.posY))

    pontos = font.render("Pontos: " + str(millenium.pontos), True, (255, 255, 255))
    vidas = font.render("Vidas: " + str(millenium.vida), True, (255, 255, 255))
    screen.blit(vidas, (60, 20))
    screen.blit(pontos, (900, 20))

    pygame.display.flip()
