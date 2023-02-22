import pygame
from random import randint
import time


preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
vermelho = (255, 100, 100)
vermelho_escuro = (200, 0, 0)
amarelo = (255, 255, 150)
amarelo_escuro = (255, 200, 0)
verde = (100, 255, 100)
verde_escuro = (0, 200, 0)
azul = (150, 150, 255)
azul_escuro = (0, 0, 255)

pygame.mixer.init()

som_play = pygame.mixer.Sound('Play.mp3')
som_fim = pygame.mixer.Sound('Fim.mp3')
som_verde = pygame.mixer.Sound('C.mp3')
som_vermelho = pygame.mixer.Sound('D.mp3')
som_amarelo = pygame.mixer.Sound('E.mp3')
som_azul = pygame.mixer.Sound('F.mp3')

window = pygame.display.set_mode((600, 600))
window.fill(branco)

pygame.font.init()
fonte = pygame.font.SysFont('Arial', 38)

is_click = True
repeticao = True
sequencia = []
resposta = []


def inicio(jan):
    global texto
    pygame.draw.rect(jan, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


def b_verde(jan):
    global texto
    pygame.draw.rect(jan, verde, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


def b_vermelho(jan):
    global texto
    pygame.draw.rect(jan, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


def b_amarelo(jan):
    global texto
    pygame.draw.rect(jan, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


def b_azul(jan):
    global texto
    pygame.draw.rect(jan, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


def b_centro(jan):
    global texto
    pygame.draw.rect(jan, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(jan, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(jan, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(jan, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(jan, preto, (100, 300, 400, 10))
    pygame.draw.rect(jan, preto, (300, 100, 10, 400))
    pygame.draw.circle(jan, branco, (300, 300), 300, 100)
    pygame.draw.circle(jan, preto, (300, 300), 90)
    pygame.draw.circle(jan, preto, (300, 300), 210, 10)
    pygame.draw.circle(jan, cinza, (300, 300), 80)
    texto = fonte.render('GENIUS', True, branco)
    jan.blit(texto, (241, 277))
    pygame.display.update()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mouse = pygame.mouse.get_pos()
    posicao_mouse = ((mouse[0] - 300) ** 2) + ((mouse[1] - 300) ** 2)
    click = pygame.mouse.get_pressed()

    if not sequencia:
        pygame.draw.rect(window, branco, (0, 0, 500, 50))
        texto = fonte.render(f'Clique no centro para iniciar', True, preto)
        window.blit(texto, (10, 10))
        pygame.display.update()

    if repeticao:
        inicio(window)
        time.sleep(1)
        for i in range(len(sequencia)):
            pygame.draw.rect(window, branco, (0, 0, 500, 50))
            texto = fonte.render(f'Fase {len(sequencia)}', True, preto)
            window.blit(texto, (10, 10))
            pygame.display.update()

            if sequencia[i] == 0:
                b_verde(window)
                som_verde.play()
            if sequencia[i] == 1:
                b_vermelho(window)
                som_vermelho.play()
            if sequencia[i] == 2:
                b_amarelo(window)
                som_amarelo.play()
            if sequencia[i] == 3:
                b_azul(window)
                som_azul.play()

            time.sleep(1)
            inicio(window)
            time.sleep(0.1)
        repeticao = False

    if resposta == sequencia and sequencia != []:
        repeticao = 1
        sequencia.append(randint(0, 3))
        resposta = []

    if (len(resposta) > 0 and len(sequencia)) > 0 and \
            resposta[-1] != sequencia[len(resposta) - 1] and sequencia != []:
        pygame.draw.rect(window, branco, (0, 0, 500, 50))
        texto = fonte.render(f'Você chegou até a fase {len(sequencia) - 1}', True, vermelho)
        window.blit(texto, (10, 10))
        som_fim.play()
        pygame.display.update()
        time.sleep(3)
        sequencia = []
        resposta = []

    if 8100 <= posicao_mouse <= 40000:
        if 100 <= mouse[0] <= 300 and 100 <= mouse[1] <= 300:
            b_verde(window)
            if click[0] == False and is_click == True:
                resposta.append(0)
                som_verde.play()
        elif 300 <= mouse[0] <= 500 and 100 <= mouse[1] <= 300:
            b_vermelho(window)
            if click[0] == False and is_click == True:
                resposta.append(1)
                som_vermelho.play()
        elif 100 <= mouse[0] <= 300 and 300 <= mouse[1] <= 500:
            b_amarelo(window)
            if click[0] == False and is_click == True:
                resposta.append(2)
                som_amarelo.play()
        elif 300 <= mouse[0] <= 500 and 300 <= mouse[1] <= 500:
            b_azul(window)
            if click[0] == False and is_click == True:
                resposta.append(3)
                som_azul.play()

    elif posicao_mouse <= 6400:
        if not sequencia:
            b_centro(window)
            if click[0] == False and is_click == True:
                som_play.play()
                repeticao = True
                sequencia.append(randint(0, 3))
                resposta = []
    else:
        inicio(window)

    pygame.draw.rect(window, branco, (0, 0, 500, 50))
    texto = fonte.render(f'{len(sequencia)}', True, preto)

    is_click = click[0]

    pygame.display.update()
