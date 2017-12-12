# -*-coding: UTF-8-*-
import pygame
import random


class Nave():  # Definição da Nave
    def __init__(self):

        self.img = pygame.image.load("./millenium.png")
        self.velocidade = 0
        self.velocidadeY = 0
        self.posX = 580
        self.posY = 700
        self.Rect = pygame.Rect(self.posX, self.posY, 100, 96)
        self.vida = 10
        self.pontos = 0

    def moveNave(self):  # Movimentação da Nave
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


class Tiro():  # Definição do Tiro
    def __init__(self, posX, posY):

        self.img = pygame.image.load("./shoot.png")
        self.posX = posX + 40
        self.posY = posY
        self.Rect = pygame.Rect(self.posX, self.posY, 30, 15)

    def refreshPos(self):  # posição do Tiro na tela e Rect de colisão
        self.posY -= 20
        self.Rect = pygame.Rect(self.posX, self.posY, 30, 15)


class Meteoro():  # Definição do Meteoro
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

    def refreshPos(self):  # Movimentação e Rotação do Meteoro
        self.posY += self.velo
        self.angulo += self.rotate

    def Carimbo(self):  # Printando a rotação, movimentação e o tamanho do meteoro na tela e Rect de colisão
        tamw = self.img.get_rect().width
        tamh = self.img.get_rect().height
        img = pygame.transform.scale(self.img, (self.size*tamw, self.size*tamh))
        img = pygame.transform.rotate(img, self.angulo)
        self.screen.blit(img, (self.posX, self.posY))
        self.Rect = pygame.Rect(self.posX, self.posY, self.size*tamw, self.size*tamh)


pygame.mixer.pre_init(44100, -16, 2, 2048)  # Mixer do som
pygame.mixer.init()
pygame.init()

font = pygame.font.SysFont(None, 60, bold=False, italic=False)  # Fonte de texto
screen = pygame.display.set_mode((1200, 800), 0, 32)  # Tamanho da tela
titulo = pygame.image.load("./titulo.png")  # Imagem do titulo do jogo
gameover = pygame.image.load("./gameover.png")  # Imagem da tela do GameOver
menuimg = pygame.image.load("./menu.png")  # Imagem da tele do Menu
pygame.mixer.music.load("musica1.ogg")  # Música do jogo
tiro_sound = pygame.mixer.Sound("musica2.wav")  # Som do tiro
explosao_sound = pygame.mixer.Sound("explosion.wav")  # Som da explosão
batida_sound = pygame.mixer.Sound("batida.wav")  # Som do choque entre a Nave e o Asteriode
clock = pygame.time.Clock()
fundo = pygame.image.load("./fundo1.jpg")  # Imagem de fundo do Jogo
pygame.mixer.music.play(-1)  # Mixer do Play da Música
finish = False

while finish is False:  # Loop das listas e chamada da Nave

    tiros = []
    meteoritos = []
    millenium = Nave()
    tiro = None
    meteorito = None
    rodando = False
    menu = True

    while menu:  # Menu

        screen.blit(menuimg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            moveNave = pygame.key.get_pressed()
            if moveNave[pygame.K_SPACE]:
                menu = False
                rodando = True

    while rodando:  # Jogo executando
            clock.tick(30)

            screen.blit(fundo, (0, 0))
            for event in pygame.event.get():  # ESC para sair do jogo
                if (event.type == pygame.QUIT):
                    exit()
                moveNave = pygame.key.get_pressed()  # Atirando
                if moveNave[pygame.K_SPACE]:
                    tiros.append(Tiro(millenium.posX, millenium.posY))
                    tiro_sound.play(0)
                elif moveNave[pygame.K_ESCAPE]:
                    exit()

            met = random.randint(0, 1000)  # Algoritimo da queda dos asteriodes na tela
            if met > 1000 - 20 - (millenium.pontos / 2):  # Difculdade conforme pontuação
                meteoritos.append(Meteoro(random.randint(1, 1120), screen))

            millenium.moveNave()  # Movimentação da Nava

            for tiro in tiros:  # Movimentação do tiro na tela guardado em lista
                tiro.refreshPos()
                screen.blit(tiro.img, (tiro.posX, tiro.posY))
                if tiro.posY < -40:  # Remoção do tiro após sair da tela do jogo
                    tiros.remove(tiro)

            for meteorito in meteoritos:  # Movimentação do asteroide guardado em lista
                meteorito.refreshPos()
                meteorito.Carimbo()
                if meteorito.posY > 800:  # Remoçã do asterioide após sair da tela
                    meteoritos.remove(meteorito)
                if meteorito.Rect.colliderect(millenium.Rect):  # Colisão do asteroide com a nave
                    meteoritos.remove(meteorito)
                    millenium.vida -= 1
                    batida_sound.play(0)
                    if millenium.vida == 0:
                        finish = True

            for meteorito in meteoritos:  # Colisão do asteroide com o tiro e soma na pontuação
                for tiro in tiros:
                    if meteorito.Rect.colliderect(tiro.Rect):
                        tiros.remove(tiro)
                        meteorito.vida -= 1
                        if meteorito.vida == 0:
                            meteoritos.remove(meteorito)
                            millenium.pontos += 1
                            explosao_sound.play(0)

            while finish:  # Tela do GameOver
                screen.blit(gameover, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                            exit()
                    moveNave = pygame.key.get_pressed()
                    if moveNave[pygame.K_ESCAPE]:
                        exit()
                    elif moveNave[pygame.K_SPACE]:
                        millenium.vida = 10
                        millenium.pontos = 0
                        millenium.posX = 580
                        millenium.posY = 700
                        tiros = []
                        meteoritos = []
                        finish = False

            screen.blit(millenium.img, (millenium.posX, millenium.posY))  # Print da Nave

            pontos = font.render("Pontos: " + str(millenium.pontos), True, (255, 255, 255))  # Texto Pontuação
            vidas = font.render("Vidas: " + str(millenium.vida), True, (255, 255, 255))  # Texto da Vida
            screen.blit(vidas, (60, 20))  # Print da Vida
            screen.blit(pontos, (900, 20))  # Print da Pontuação
            screen.blit(titulo, (440, 20))  # Print do Título do jogo
            pygame.display.flip()
