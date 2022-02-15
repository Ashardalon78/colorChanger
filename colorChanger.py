import pygame
import tkinter as tk
from tkinter import filedialog
import os.path as op


class ColorChanger():
	pygame.init()
	pygame.display.set_mode((200, 150))
	def __init__(self):		
		
		self.master = tk.Tk()
		self.master.geometry("384x128")
		self.master.title("Color changer by Ashardalon78")

		tk.Label(self.master,text="Red threshold:").grid(row=0,column=0)
		self.T1 = tk.Text(self.master,height=1,width=5)
		self.T1.grid(row=0,column=1)
		self.T1.insert(tk.END,50)
		tk.Label(self.master,text="Green threshold:").grid(row=1,column=0)
		self.T2 = tk.Text(self.master,height=1,width=5)
		self.T2.grid(row=1,column=1)
		self.T2.insert(tk.END,50)
		tk.Label(self.master,text="Blue threshold:").grid(row=2,column=0)
		self.T3 = tk.Text(self.master,height=1,width=5)
		self.T3.grid(row=2,column=1)
		self.T3.insert(tk.END,50)
		
		tk.Label(self.master,text="Red adjust:").grid(row=0,column=2)
		self.T4 = tk.Text(self.master,height=1,width=5)
		self.T4.grid(row=0,column=3)
		self.T4.insert(tk.END,150)
		tk.Label(self.master,text="Green adjust:").grid(row=1,column=2)
		self.T5 = tk.Text(self.master,height=1,width=5)
		self.T5.grid(row=1,column=3)
		self.T5.insert(tk.END,0)
		tk.Label(self.master,text="Blue adjust:").grid(row=2,column=2)
		self.T6 = tk.Text(self.master,height=1,width=5)
		self.T6.grid(row=2,column=3)
		self.T6.insert(tk.END,0)
		
		self.C1 = tk.IntVar()
		tk.Checkbutton(self.master, text="Use Threshold greater than", variable=self.C1).grid(row=3, column=1)
				
		tk.Button(self.master, text="Load Image", command=self.load_image).grid(row=3, column=0)
		tk.Button(self.master, text="Start", command=self.adjust_colors).grid(row=4, column=0)		

		self.master.mainloop()				
		
	def load_image(self):				
		imgInFile = open(filedialog.askopenfilename(title = "Select image file",filetypes = (("png Files","*.png"),("all files","*.*"))),'rb')
		if not imgInFile:
			return	
												
		self.img = pygame.image.load(imgInFile).convert()
		# sprite_red = self.reduce_sprite(sprite)
		# pygame.image.save(sprite_red, op.join(root,name))
					
	def adjust_colors(self):
		red_thresh = int(self.T1.get('1.0',tk.END))
		green_thresh = int(self.T2.get('1.0',tk.END))
		blue_thresh = int(self.T3.get('1.0',tk.END))
		red_adjust = int(self.T4.get('1.0',tk.END))
		green_adjust = int(self.T5.get('1.0',tk.END))
		blue_adjust = int(self.T6.get('1.0',tk.END))
		rev_thresh = self.C1.get()		
		
		width = self.img.get_width()
		height = self.img.get_height()			
		for i in range(width):
			for j in range(height):
				color = self.img.get_at((i, j))			
				if rev_thresh:
					condition = color[0] > red_thresh and color[1] > green_thresh and color[2] > blue_thresh					
				else:
					condition = color[0] < red_thresh and color[1] < green_thresh and color[2] < blue_thresh
									
				if condition:
					if red_adjust >=0: new_red = min(255, color[0]+red_adjust)
					else: new_red = max(0, color[0]+red_adjust)
					if green_adjust >=0: new_green = min(255, color[1]+green_adjust)
					else: new_green = max(0, color[1]+green_adjust)
					if blue_adjust >=0: new_blue = min(255, color[2]+blue_adjust)
					else: new_blue = max(0, color[2]+blue_adjust)
					#new_color = (new_red,new_green,new_blue,color[3])					
					#new_color = tuple(map(sum,zip(color,(new_red,new_green,new_blue,0))))
					new_color = [new_red,new_green,new_blue]
					if len(color)>=4: new_color.append(color[3])
					new_color = tuple(new_color)
					self.img.set_at((i, j), new_color)					
						
				
		imgOutFile = filedialog.asksaveasfilename(title = "Save image file",filetypes = (("png Files","*.png"),("all files","*.*")),defaultextension='.png')
		#print(imgOutFile)
		pygame.image.save(self.img, imgOutFile)
	
CC = ColorChanger()