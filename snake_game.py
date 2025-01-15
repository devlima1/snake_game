import pygame
from pygame.locals import *
import random

# Tamanho do pixel e tamanho da janela
PIXEL_SIZE = 10
WINDOW_SIZE = (600, 600)

# Função para verificar colisão entre duas posições
def collision(pos1, pos2):
    return pos1 == pos2

# Função para verificar se a posição está fora dos limites da janela
def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

# Função para gerar uma posição aleatória da maçã dentro da grid
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

# Inicialização da tela do Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake Game')

# Posições inicias da cobra e sua superfície
snake_pos = [(250, 50), (260, 50), (270, 50)] # A cobra começou com 3 segmentos
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE)) # Superfície da cobra
snake_surface.fill((0, 255, 0)) # Cor da cobra (verde)
snake_direction = K_LEFT # Direção inicial da cobra (para a esquerda)

# Posições da maçã e sua superfície 
apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE)) # Superfície da maçã
apple_surface.fill((255, 0, 0)) # Cor da maçã (vermelha)
apple_pos = random_on_grid() # Gera a posição inicial da maçã

# Condição para manter a janela aberta
running = True
while running:
    pygame.time.Clock().tick(15) # Controla a taxa de atualização do jogo (frame rate)
    screen.fill((0, 0, 0)) # Limpa a tela (preenche com cor preta)

    # Loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Fecha o jogo
            running = False
        elif event.type == KEYDOWN: # Define a direção da cobra com base na tecla pressionada
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key
    
    # Desenha a maçã na tela
    screen.blit(apple_surface, apple_pos)
    
    # Verifica colisão da cobra com a maçã e faz a cobra crescer
    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10)) # A cobra cresce
        apple_pos = random_on_grid() # A maçã muda de posição

    # Desenha a cobra na tela
    for pos in snake_pos:
        screen.blit(snake_surface, pos)
    
    # Atualiza o corpo da cobra (faz com que o corpo siga a cabeça)
    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]): # Verifica se a cobra colide com ela mesma
            running = False # Finaliza o jogo
        snake_pos[i] = snake_pos[i-1]
    
    # Verifica se a cobra ultrapassa os limites da tela
    if off_limits(snake_pos[0]):
        running = False # Finaliza o jogo
    
    # Atualiza a posição da cabeça da cobra com base na direção
    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    # Atualiza a tela
    pygame.display.update()