#utilizei o pygame,sys e randint da biblioteca random
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
#velocidade do game
relogio = pygame.time.Clock()

#musica que serão utilizadas
musica_fundo = pygame.mixer.music.load('BoxCat Games - Victory.mp3')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

musica_pontos = pygame.mixer.Sound("smw_fireball.wav")
musica_pontos.set_volume(0.75)
# posição da maça
xm = randint(40,500)
ym = randint(40,420)

# definição de tela e seu tamanho
laguraT = 640
alturaT = 480
tela = pygame.display.set_mode((laguraT,alturaT))
#definição da posição da cobra
xc = laguraT/2 - 40/2
yc = alturaT/2 - 50/2
velocidade = 10
x_controle = velocidade
y_controle = 0
# definindo o nome da janela
pygame.display.set_caption("SNAKER")

# mostra a pontuação na tela
fonte_tela = pygame.font.SysFont("arial", 17, True, True)
ponto = 0
#criação de uma função para tratar as lista de posições
lista_cobra = []
#criação de uma lista que receberar a posição inicial da cobra
comprimento_inicial = 5
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
#XeY é uma lista com os valores [x,y]
#XeY[0] = x
#XeY[1] = y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 25, 25))

#crianção do loop infinito com condições dentro

while True:
    contador = f'sua pontuação atual é {ponto}'
    relogio.tick(30)
    texto_cont_formatado = fonte_tela.render(contador, False, (255,255,255) )
    #cor da tela
    tela.fill((0,0,0))
#crianção de um for onde tera as condições evento
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_controle = -velocidade
                y_controle = 0
            elif event.key == K_d:
                x_controle = velocidade
                y_controle = 0
            elif event.key == K_w:
                y_controle = -velocidade
                x_controle = 0
            elif event.key == K_s:
                y_controle = velocidade
                x_controle = 0
    xc = xc + x_controle
    yc = yc + y_controle

# criação da cobra
    cobra = pygame.draw.rect(tela, (0,255,0), (xc,yc, 25, 25))
#criação de uma lista para armazenar a posição onde ela se encontra
    lista_cabeca = []
    lista_cabeca.append(xc)
    lista_cabeca.append(yc)
    lista_cobra.append(lista_cabeca)
    aumenta_cobra(lista_cobra)
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]


#criação da mança
    maca = pygame.draw.circle(tela, (255,0,0), (xm,ym), 5)
# criação da colisão com a adição da pontuação
    if cobra.colliderect(maca):
        ponto = ponto + 1
        xm = randint(40,630)
        ym = randint(50,430)
        musica_pontos.play()
        comprimento_inicial += 1
    tela.blit(texto_cont_formatado, (400, 40))
    pygame.display.update()
