# @autor: Magno Efren - 2022
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Tk, Frame, Canvas
from itertools import product
from math import cos, sin 
from random import choice
import numpy as np 

class Cube(Frame):
	def __init__(self, master):
		super().__init__(master)

		self.canvas = Canvas(master, bg = 'black')
		self.canvas.place(relx = 0, rely=0, relwidth= 1, relheight=1)

		self.points = []
		self.scale = 120
		self.objects_points = []
		self.objects_lines = []
		self.theta = 0
		self.position = [500,300]

		for point in product((-1,1), repeat = 3):
			self.points.append(np.array(point))

		self.projection_matrix = np.array([[1,0,0], [0,1,0]])
		self.xy = [[n,n] for n in range(len(self.points))]

		self.create_obj()
		self.update()

	def create_obj(self):
		for i in range(8):
			obj = self.canvas.create_text(0,i, font = ('Arial', 100))
			self.objects_points.append(obj)
		for i in range(12):
			obj1 = self.canvas.create_line(0,0,0,0)
			self.objects_lines.append(obj1)

	def draw_points(self, obj, char, x,y, color):
		self.canvas.itemconfig(obj, fill = color, text = char)
		self.canvas.coords(obj, x,y)

	def connect_points(self, obj, i, j, xy, color):
		self.canvas.itemconfig(obj, fill = color, width = 5)
		self.canvas.coords(obj, xy[i][0], xy[i][1], xy[j][0], xy[j][1])

	def update(self):
		rotation_x = np.array([[1,0,0], [0,cos(self.theta), - sin(self.theta)], 
			[0, sin(self.theta), cos(self.theta)]])

		rotation_y  = np.array([[cos(self.theta), 0, sin(self.theta)], [0,1,0],
			[-sin(self.theta), 0, cos(self.theta)]])

		rotation_z = np.array([[cos(self.theta), -sin(self.theta), 0],
			[sin(self.theta), cos(self.theta),0], [0,0,1]])

		self.theta +=0.06
		color = choice(['red', 'blue', 'aqua', 'magenta', 'green2', 'yellow'])

		for i, point in enumerate(self.points):
			rotated = np.dot(rotation_z, point.reshape((3,1)))
			rotated = np.dot(rotation_y, rotated)
			rotated = np.dot(rotation_x, rotated) 
			projected = np.dot(self.projection_matrix, rotated)

			x = int(projected[0][0]*self.scale)+self.position[0]
			y = int(projected[1][0]*self.scale) + self.position[1]

			self.draw_points(self.objects_points[i], '•', x,y, color)

			self.xy[i] = [x,y]

			for k in range(4):
				self.connect_points(self.objects_lines[k], k, (k+4), self.xy, color)
				self.connect_points(self.objects_lines[k+4], (k+2), ((k%4)+(k//2)+3*(k//2)), 
					self.xy, color)
				self.connect_points(self.objects_lines[k+8], (k%4)*2, (k%4)*2+1, 
					self.xy, color)
		self.master.after(200, self.update)

if __name__ =='__main__':
	root = Tk()
	root.title('Cube Animation')
	root.geometry('1000x600')
	app = Cube(root)
	app.mainloop()