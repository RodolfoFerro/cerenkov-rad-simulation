#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pygame, sys
from pygame.locals import *
from tkinter import *

# Default variables:
refindex1 = 1.0 		# Refraction index 1
refindex2 = 1.0 		# Refraction index 1
col1 = (255,229,204)	# Color 1
col2 = (255,255,204)	# Color 1
c  = 3 					# Light's speed in void
v = int((0.9999)*c) 	# Particle's speed in a medium


# Function to detect if click was inside of the button:
def inButton(x,y,x1,y1,x2,y2):
	if x >= x1 and x <= x2 and y >= y1 and y <=y2:
		return True
	return False

# Create surfaces for simulations:
def defineSurface(size,color):
	surf = pygame.Surface(size)
	surf = surf.convert()
	surf.fill(color)
	return surf

# Funcition to move a particle in a surface:
def moveParticle(initx, posx, posy, color, r, surface, background_col, trace_width, trace_col, rads, vl):
	surface.fill(background_col)
	pygame.draw.line(surface,trace_col, (initx, posy), (posx, posy), trace_width)
	n = len(rads)
	for i in range(n):
		if posx >= rads[i][0]:
			pygame.draw.circle(surface,trace_col,(rads[i][0],posy),int(vl*rads[i][1])+1,trace_width)
			rads[i][1] += 0.03
	pygame.draw.circle(surface,color,(posx,posy),r)
	pygame.display.update()

# Update surface after moving ended:
def updateSurface(window, surface, color, initx, pos, rad, coord, trace_col, trace_width, rads, vl):
	pygame.draw.line(surface,trace_col, (initx, pos[1]), pos, trace_width)
	n = len(rads)
	for i in range(n):
		if pos[0] >= rads[i][0]:
			pygame.draw.circle(surface,trace_col,(rads[i][0],pos[1]),int(vl*rads[i][1])+1,trace_width)
	pygame.draw.circle(surface,color,pos,rad)
	window.blit(surface,coord)

# Function to ask for the refraction index:
def inputData():
	global refindex1, refindex2, col1, col2
	top = Tk()
	top.title("Setting refraction index")

	def setVars():
		global refindex1, refindex2, col1, col2
		refindex1 = n1.get()
		refindex2 = n2.get()
		col1 = (255,229,204)
		col2 = (255,255,204)
		top.destroy()

	# Simulation 1
	labelframe1 = LabelFrame(top, text="Simulation 1:")
	labelframe1.pack(fill="both", expand="yes")

	frameD1 = Frame(labelframe1)
	frameD1.pack()

	LD1 = Label(frameD1, text = "Set the refraction index: ",fg="white")
	LD1.pack(side = LEFT)

	n1 = DoubleVar()
	n1.set(1.)
	ED1 = Entry(frameD1,bd=1,textvariable=n1,width=15,fg="navy",bg="white")
	ED1.pack(side = LEFT)

	# Simulation 2
	labelframe2 = LabelFrame(top, text="Simulation 2:")
	labelframe2.pack(fill="both", expand="yes")

	frameD2 = Frame(labelframe2)
	frameD2.pack()

	LD2 = Label(frameD2, text = "Set the refraction index: ",fg="white")
	LD2.pack(side = LEFT)

	n2 = DoubleVar()
	n2.set(1.)
	ED2 = Entry(frameD2,bd=1,textvariable=n2,width=15,fg="navy",bg="white")
	ED2.pack(side = LEFT)

	B = Button(top,text="Accept",fg="white",command=setVars)
	B.pack(side=RIGHT)

	top.mainloop()

# Function to select from preloaded data:
def preloadedData():
	global refindex1, refindex2, col1, col2
	def sel1():
		global refindex1, col1
		if indx1.get() == 1:
			refindex1 = 1.44
			col1 = (220,220,220)
		elif indx1.get() == 2:
			refindex1 = 1.0002926
			col1 = (255,255,255)
		elif indx1.get() == 3:
			refindex1 = 1.385
			col1 = (173,255,47)
		elif indx1.get() == 4:
			refindex1 = 1.635
			col1 = (0,0,0)
		elif indx1.get() == 5:
			refindex1 = 1.32
			col1 = (240,255,255)
		elif indx1.get() == 6:
			refindex1 = 1.3329
			col1 = (240,248,255)
		elif indx1.get() == 7:
			refindex1 = 1.515
			col1 = (255,255,240)
		elif indx1.get() == 8:
			refindex1 = 1.46
			col1 = (248,248,255)
		elif indx1.get() == 9:
			refindex1 = 2.5
			col1 = (169,169,169)
		elif indx1.get() == 10:
			refindex1 = 1.624
			col1 = (47,79,79)
		selection1 = "The refraction index is " + str(refindex1)
		label1.config(text = selection1)

	def sel2():
		global refindex2, col2
		if indx2.get() == 1:
			refindex2 = 1.44
			col2 = (220,220,220)
		elif indx2.get() == 2:
			refindex2 = 1.0002926
			col2 = (255,255,255)
		elif indx2.get() == 3:
			refindex2 = 1.385
			col2 = (173,255,47)
		elif indx2.get() == 4:
			refindex2 = 1.635
			col2 = (0,0,0)
		elif indx2.get() == 5:
			refindex2 = 1.32
			col2 = (240,255,255)
		elif indx2.get() == 6:
			refindex2 = 1.3329
			col2 = (240,248,255)
		elif indx2.get() == 7:
			refindex2 = 1.515
			col2 = (255,255,240)
		elif indx2.get() == 8:
			refindex2 = 1.46
			col2 = (248,248,255)
		elif indx2.get() == 9:
			refindex2 = 2.5
			col2 = (169,169,169)
		elif indx2.get() == 10:
			refindex2 = 1.624
			col2 = (47,79,79)
		selection2 = "The refraction index is " + str(refindex2)
		label2.config(text = selection2)

	def setVars():
		root.destroy()

	root = Tk()
	root.title("Material selection")
	indx1 = DoubleVar()
	indx2 = DoubleVar()

	# Simulation 1
	root1 = LabelFrame(root, text="Simulation 1:")
	root1.pack(fill="both", expand="yes")

	# Aluminium
	R1 = Radiobutton(root1, text="Aluminium", variable=indx1, value=1, command=sel1)
	R1.pack( anchor = W )
	# Air
	R2 = Radiobutton(root1, text="Air", variable=indx1, value=2, command=sel1)
	R2.pack( anchor = W )
	# Liquid chlorine
	R3 = Radiobutton(root1, text="Liquid chlorine", variable=indx1, value=3, command=sel1)
	R3.pack( anchor = W)
	# Asphalt
	R4 = Radiobutton(root1, text="Asphalt", variable=indx1, value=4, command=sel1)
	R4.pack( anchor = W )
	# Ice
	R5 = Radiobutton(root1, text="Ice", variable=indx1, value=5, command=sel1)
	R5.pack( anchor = W )
	# Water
	R6 = Radiobutton(root1, text="Water", variable=indx1, value=6, command=sel1)
	R6.pack( anchor = W)
	# Oil
	R7 = Radiobutton(root1, text="Oil", variable=indx1, value=7, command=sel1)
	R7.pack( anchor = W )
	# Glass
	R8 = Radiobutton(root1, text="Glass", variable=indx1, value=8, command=sel1)
	R8.pack( anchor = W )
	# Steel
	R9 = Radiobutton(root1, text="Steel", variable=indx1, value=9, command=sel1)
	R9.pack( anchor = W)
	# Tourmaline
	R10 = Radiobutton(root1, text="Tourmaline", variable=indx1, value=10, command=sel1)
	R10.pack( anchor = W)

	label1 = Label(root1)
	label1.pack()

	# Simulation 2
	root2 = LabelFrame(root, text="Simulation 2:")
	root2.pack(fill="both", expand="yes")

	# Aluminium
	R1 = Radiobutton(root2, text="Aluminium", variable=indx2, value=1, command=sel2)
	R1.pack( anchor = W )
	# Air
	R2 = Radiobutton(root2, text="Air", variable=indx2, value=2, command=sel2)
	R2.pack( anchor = W )
	# Liquid chlorine
	R3 = Radiobutton(root2, text="Liquid chlorine", variable=indx2, value=3, command=sel2)
	R3.pack( anchor = W)
	# Asphalt
	R4 = Radiobutton(root2, text="Asphalt", variable=indx2, value=4, command=sel2)
	R4.pack( anchor = W )
	# Ice
	R5 = Radiobutton(root2, text="Ice", variable=indx2, value=5, command=sel2)
	R5.pack( anchor = W )
	# Water
	R6 = Radiobutton(root2, text="Water", variable=indx2, value=6, command=sel2)
	R6.pack( anchor = W)
	# Oil
	R7 = Radiobutton(root2, text="Oil", variable=indx2, value=7, command=sel2)
	R7.pack( anchor = W )
	# Glass
	R8 = Radiobutton(root2, text="Glass", variable=indx2, value=8, command=sel2)
	R8.pack( anchor = W )
	# Steel
	R9 = Radiobutton(root2, text="Steel", variable=indx2, value=9, command=sel2)
	R9.pack( anchor = W)
	# Tourmaline
	R10 = Radiobutton(root2, text="Tourmaline", variable=indx2, value=10, command=sel2)
	R10.pack( anchor = W)

	label2 = Label(root2)
	label2.pack()

	B = Button(root,text="Accept",fg="white",command=setVars)
	B.pack(side=RIGHT)

	root.mainloop()
	
# Main:
def main():
	global v
	X = 800
	Y = 640 
	# Initialize window size and title:
	pygame.init()
	window = pygame.display.set_mode((X,Y))
	pygame.display.set_caption("Cerenkov Radiation Simulation")
	init = 0
	state = 1
	s1p1 = (35,40)
	s1p2 = (382,296)
	s2p1 = (419,40)
	s2p2 = (766,296)
	while True:
		# We define the background and button coordenates
		# depending on the state where we are.
		if state == 1:
			background = pygame.image.load("splash screen.png")
			p1 = (276,449)
			p2 = (524,515)
		elif state == 2:
			background = pygame.image.load("info.png")
			p1 = (52,505)
			p2 = (299,569)
			p3 = (500,505)
			p4 = (748,569)
		elif state == 3:
			background = pygame.image.load("select.png")
			p1 = (35,543)
			p2 = (267,603)
			p3 = (532,543)
			p4 = (764,603)
			Bb1 = (36,41)
			Bb2 = (766,256)
			Bb3 = (36,293)
			Bb4 = (766,507)
		elif state == 4:
			background = pygame.image.load("sim.png")
			p1 = (35,543)
			p2 = (267,603)
			p3 = (532,543)
			p4 = (764,603)
			surf1 = defineSurface((s1p2[0]-s1p1[0],s1p2[1]-s1p1[1]),col1) 	# Surface for 1st sim
			surf2 = defineSurface((s2p2[0]-s2p1[0],s2p2[1]-s2p1[1]),col2) 	# Surface for 2nd sim
		elif state == 5:
			background = pygame.image.load("credits.png")
			p1 = (0,0)
			p2 = (X,Y)
		# Fill background on the window:
		window.blit(background,(0,0))
		if state == 4:
			if init == 0:
				x1 = 0
				y1 = (s1p2[1] - s1p1[1]) / 2
				x2 = 0
				y2 = (s2p2[1] - s2p1[1]) / 2
				init = 1
				initx1 = x1
				initx2 = x2
				rads1 = [ [i,0] for i in range(x1, s1p2[0]-100) if i%20 == 0]
				rads2 = [ [i,0] for i in range(x1, s1p2[0]-100) if i%20 == 0]
			while x1 < s1p2[0]-100:
				moveParticle(initx1,int(x1),y1,(255,0,0),3,surf1,col1,1,(204,0,204),rads1,v)
				window.blit(surf1,s1p1)
				moveParticle(initx2,int(x2),y2,(255,0,0),3,surf2,col2,1,(204,0,204),rads2,v)
				window.blit(surf2,s2p1)
				x1 += 0.1*v
				x2 += 0.1*v
			updateSurface(window,surf1,(255,0,0),initx1,(int(x1),y1),3,s1p1,(204,0,204),1,rads1,v)
			updateSurface(window,surf2,(255,0,0),initx2,(int(x2),y2),3,s2p1,(204,0,204),1,rads2,v)
		# Check events on window:
		for event in pygame.event.get():
			# Closing the window
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# Pressing esc
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					pygame.quit()
					sys.exit()
			# Detecting clicks to change the state
			elif event.type == pygame.MOUSEBUTTONUP:
				if state == 1:
					pA = pygame.mouse.get_pos()
					if inButton(pA[0],pA[1],p1[0],p1[1],p2[0],p2[1]):
						state = 2
				elif state == 2:
					pA = pygame.mouse.get_pos()
					if inButton(pA[0],pA[1],p1[0],p1[1],p2[0],p2[1]):
						state = 1
					elif inButton(pA[0],pA[1],p3[0],p3[1],p4[0],p4[1]):
						state = 3
				elif state == 3:
					pA = pygame.mouse.get_pos()
					if inButton(pA[0],pA[1],p1[0],p1[1],p2[0],p2[1]):
						state = 2
					elif inButton(pA[0],pA[1],p3[0],p3[1],p4[0],p4[1]):
						state = 4
					elif inButton(pA[0],pA[1],Bb1[0],Bb1[1],Bb2[0],Bb2[1]):
						preloadedData()
					elif inButton(pA[0],pA[1],Bb3[0],Bb3[1],Bb4[0],Bb4[1]):
						inputData()
				elif state == 4:
					pA = pygame.mouse.get_pos()
					if inButton(pA[0],pA[1],p1[0],p1[1],p2[0],p2[1]):
						state = 3
						init = 0
					elif inButton(pA[0],pA[1],p3[0],p3[1],p4[0],p4[1]):
						state = 5
				elif state == 5:
					pA = pygame.mouse.get_pos()
					if inButton(pA[0],pA[1],p1[0],p1[1],p2[0],p2[1]):
						pygame.quit()
						sys.exit()
				
		# Update window: 
		pygame.display.update()
		#print pygame.mouse.get_pos()


if __name__ == '__main__':
	main()
