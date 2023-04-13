import pygame
from pygame.locals import *
import random
import networkx as nx

size = width, height = (430, 430)

# Configurações do tabuleiro
square_size = 50
square_margin = 3
board_width = 8 * square_size + 9 * square_margin
board_height = 8 * square_size + 9 * square_margin

# cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (128, 128, 128)
yellow = (255, 255, 30)
blue = (0, 0, 255)
pink = (255, 20, 147)

pygame.init()
running = True
# Define o tamanho da tela
screen = pygame.display.set_mode(size)
# Define o título da janela
pygame.display.set_caption("Encontre o caminha!")
# Define o background
screen.fill(green)

# delimita o tabuleiro
pygame.draw.rect(screen, green, (0,0, width, height), 5)

# cria tabuleiro
def createBoard(linhas, colunas):
    board = []
    for i in range(linhas):
        board.append([])
        for j in range(colunas):
            board[i].append(0)
            if i==0:
                board[i][j] = 5
            elif i==7:
                board[i][j] = 6
    return board

# desenha tabuleiro
def drawBoard(board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == 0:
                x = col * (square_size + square_margin) + square_margin
                y = row * (square_size + square_margin) + square_margin
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen, black, rect)
            elif board[row][col] == 1:
                x = col * (square_size + square_margin) + square_margin
                y = row * (square_size + square_margin) + square_margin
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen,red, rect)
            elif board[row][col] == 2:
                x = col * (square_size + square_margin) + square_margin
                y = row * (square_size + square_margin) + square_margin
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen, yellow, rect)
            elif board[row][col] == 5:
                x = col * (square_size + square_margin) + square_margin
                y = row * (square_size + square_margin) + square_margin
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen, blue, rect)
            elif board[row][col] == 6:
                x = col * (square_size + square_margin) + square_margin
                y = row * (square_size + square_margin) + square_margin
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(screen, pink, rect)

board = createBoard(8, 8)
player = xPlayer, yPlayer = (random.randint(0,7),7)
corLast = board[yPlayer][xPlayer]
board[yPlayer][xPlayer] = 2

while running:


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]:
                if xPlayer > 0:
                    board[yPlayer][xPlayer] = corLast
                    xPlayer -= 1
                    corLast = board[yPlayer][xPlayer]
                    board[yPlayer][xPlayer] = 2
            if event.key in [K_RIGHT, K_d]:
                if xPlayer < 7:
                    board[yPlayer][xPlayer] = corLast
                    xPlayer += 1
                    corLast = board[yPlayer][xPlayer]
                    board[yPlayer][xPlayer] = 2
            if event.key in [K_UP, K_w]:
                if yPlayer > 0:
                    board[yPlayer][xPlayer] = corLast
                    yPlayer -= 1
                    corLast = board[yPlayer][xPlayer]
                    board[yPlayer][xPlayer] = 2
            if event.key in [K_DOWN, K_s]:
                if yPlayer < 7:
                    board[yPlayer][xPlayer] = corLast
                    yPlayer += 1
                    corLast = board[yPlayer][xPlayer]
                    board[yPlayer][xPlayer] = 2
                
                
        drawBoard(board)
        pygame.display.update()

pygame.quit()