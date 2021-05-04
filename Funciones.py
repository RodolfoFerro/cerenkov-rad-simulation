#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
import math

DIMENSION_X = 800
DIMENSION_Y = 500
Y = 250
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
RED = (250, 0, 0)

iniPos = 50 # Posición inicial de la partícula
VP = 29 # Velocidad de la partícula
intervalo = 3 # Cada cuántos segundos se graficarán las ondas

n = 2.33 # Índice de refracción
c = 30 # Velocidad de la luz en el vacío
vl = int(c/n) # Velocidad de la luz en el medio
T = 17 #Periodo de tiempo para graficar.

tetha = math.acos(c/(VP*n)) # Ángulo de emisión

# Initialize window size and title:
pygame.init()
window = pygame.display.set_mode((DIMENSION_X, DIMENSION_Y))
pygame.display.set_caption("Animación efecto Cerenkov")
# Fill background
background = pygame.Surface(window.get_size())
background = background.convert()

def moveParticle(xp):
	background.fill(WHITE)
	pygame.draw.circle(window, BLACK, [xp, Y], 2)

def way(xp):
	pygame.draw.line(window, BLACK, [iniPos, Y], [xp, Y], 1)

def blueRay(origin, time, xp):
	x = vl*time*math.cos(tetha)
	x = x + origin
	y = vl*time*math.sin(tetha)
	y = y + Y
	au = 2*(y-Y)
	y = y - au
	pygame.draw.line(window, BLUE, [origin, Y], [int(x), int(y)], 2)
	pygame.draw.line(window, RED, [int(x), int(y)], [xp, Y], 2)

def waves(xp, t):
	punto = iniPos
	for i in range(iniPos, xp):
		pygame.draw.circle(window, BLACK, [punto, Y], vl*t, 1)
		blueRay(punto, t, xp)
		aux = punto + VP*intervalo
		if aux < xp:
			punto += VP*intervalo
			t -= intervalo
	
# Main:
def main():
	background.fill(WHITE)
	xp = iniPos # Posición de la partícula
	t = 0
	while True:
		# Fill background:
		while t < T:
			window.blit(background,(0,0))
			way(xp)
			moveParticle(xp)
			if t > intervalo:
				waves(xp, t)
			xp = iniPos + t*VP
			t += 1
		window.blit(background,(0,0))
		way(xp)
		moveParticle(xp)
		waves(xp, t-1)
		blueRay(iniPos, T-1, xp)


		# Check events on window:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					pygame.quit()
					sys.exit()

		# Update window: 
		pygame.display.update()

if __name__ == '__main__':
	main()
