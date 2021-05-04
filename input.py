#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

refindex1=1.
refindex2=1.

def preloadedData():
	global refindex1, refindex2
	def sel1():
	   selection1 = "The refraction index is " + str(indx1.get())
	   label1.config(text = selection1)

	def sel2():
	   selection2 = "The refraction index is " + str(indx2.get())
	   label2.config(text = selection2)

	def setVars():
		global refindex1, refindex2
		refindex1 = indx1.get()
		refindex2 = indx2.get()
		root.destroy()

	root = Tk()
	indx1 = DoubleVar()
	indx2 = DoubleVar()

	# Simulation 1
	root1 = LabelFrame(root, text="Simulation 1:")
	root1.pack(fill="both", expand="yes")

	# Aluminium
	R1 = Radiobutton(root1, text="Aluminium", variable=indx1, value=1.44, command=sel1)
	R1.pack( anchor = W )
	# Air
	R2 = Radiobutton(root1, text="Air", variable=indx1, value=1.0002926, command=sel1)
	R2.pack( anchor = W )
	# Liquid chlorine
	R3 = Radiobutton(root1, text="Liquid chlorine", variable=indx1, value=1.385, command=sel1)
	R3.pack( anchor = W)
	# Asphalt
	R4 = Radiobutton(root1, text="Asphalt", variable=indx1, value=1.635, command=sel1)
	R4.pack( anchor = W )
	# Ice
	R5 = Radiobutton(root1, text="Ice", variable=indx1, value=1.32, command=sel1)
	R5.pack( anchor = W )
	# Water
	R6 = Radiobutton(root1, text="Water", variable=indx1, value=1.3329, command=sel1)
	R6.pack( anchor = W)
	# Oil
	R7 = Radiobutton(root1, text="Oil", variable=indx1, value=1.515, command=sel1)
	R7.pack( anchor = W )
	# Glass
	R8 = Radiobutton(root1, text="Glass", variable=indx1, value=1.46, command=sel1)
	R8.pack( anchor = W )
	# Steel
	R9 = Radiobutton(root1, text="Steel", variable=indx1, value=2.5, command=sel1)
	R9.pack( anchor = W)
	# Tourmaline
	R10 = Radiobutton(root1, text="Tourmaline", variable=indx1, value=1.624, command=sel1)
	R10.pack( anchor = W)

	label1 = Label(root1)
	label1.pack()

	# Simulation 2
	root2 = LabelFrame(root, text="Simulation 2:")
	root2.pack(fill="both", expand="yes")

	# Aluminium
	R1 = Radiobutton(root2, text="Aluminium", variable=indx2, value=1.44, command=sel2)
	R1.pack( anchor = W )
	# Air
	R2 = Radiobutton(root2, text="Air", variable=indx2, value=1.0002926, command=sel2)
	R2.pack( anchor = W )
	# Liquid chlorine
	R3 = Radiobutton(root2, text="Liquid chlorine", variable=indx2, value=1.385, command=sel2)
	R3.pack( anchor = W)
	# Asphalt
	R4 = Radiobutton(root2, text="Asphalt", variable=indx2, value=1.635, command=sel2)
	R4.pack( anchor = W )
	# Ice
	R5 = Radiobutton(root2, text="Ice", variable=indx2, value=1.32, command=sel2)
	R5.pack( anchor = W )
	# Water
	R6 = Radiobutton(root2, text="Water", variable=indx2, value=1.3329, command=sel2)
	R6.pack( anchor = W)
	# Oil
	R7 = Radiobutton(root2, text="Oil", variable=indx2, value=1.515, command=sel2)
	R7.pack( anchor = W )
	# Glass
	R8 = Radiobutton(root2, text="Glass", variable=indx2, value=1.46, command=sel2)
	R8.pack( anchor = W )
	# Steel
	R9 = Radiobutton(root2, text="Steel", variable=indx2, value=2.5, command=sel2)
	R9.pack( anchor = W)
	# Tourmaline
	R10 = Radiobutton(root2, text="Tourmaline", variable=indx2, value=1.624, command=sel2)
	R10.pack( anchor = W)

	label2 = Label(root2)
	label2.pack()

	B = Button(root,text="Accept",fg="white",command=setVars)
	B.pack(side=RIGHT)

	root.mainloop()

preloadedData()
print refindex1, refindex2