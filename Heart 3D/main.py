from tkinter import Tk, Frame, Canvas 
from math import cos, sin
from random import randint  
import numpy as np 

class Heart(Frame):
	def __init__(self, master):
		super().__init__(master)

		self.canvas = Canvas(master, bg= 'black')
		self.canvas.place(relx = 0, rely = 0, relwidth = 1, relheight=1)

		self.objects = []
		self.n = 0
		self.x = 0
		self.y = 0
		self.create_obj()
		self.update()

	def create_obj(self):
		for i in range(900):
			obj = self.canvas.create_text(0,0, font= ('Arial', 18, 'bold'))
			self.objects.append(obj)

	def draw(self, obj, char, x,y, color):
		self.canvas.itemconfig(obj, fill = color, text = char)
		self.canvas.coords(obj, x+200, y+30)

	def update(self):
		zbuffer = [0]*900
		maxz = 0 
		num = 0
		chars  = " .,-~:;=!*#$@@"
		c = cos(self.n)
		s = sin(self.n)
		for y in np.arange(-0.5, 0.51, 0.01):
			r = 0.4 + 0.04*(0.4 + 0.4*sin(self.n*6 + y*2))**8
			for x in np.arange(-0.5, 0.51, 0.01):
				z = -x**2 - (1.2*y-abs(x)*(2/3))**2 + r**2
				if z>0:
					z = ((z)**(1/2))/(2-y)
					for z2 in np.arange(-z, z, z/6):
						ax = x*c - z2*s 
						az = x*s + z2*c 
						p = 1 + az/2

						px = round((ax*p + 0.5)*30)
						py = round((-y*p + 0.5)*30)

						pos = px + 30*py
						if zbuffer[pos] <= az:
							zbuffer[pos] = az
							if maxz <= az:
								maxz = az
		for i in range(30):
			self.y += 20
			for j in range(30):
				self.x += 20
				idx = int(zbuffer[num]/maxz*13)
				color = '#{:02x}{:02x}{:02x}'.format(randint(50,255), randint(50,255), randint(50,255))
				self.draw(self.objects[num], chars[idx], self.x, self.y, color)
				num += 1
			self.x = 0
		self.y = 0
		num = 0
		self.n += 0.3
		self.master.after(80, self.update)



if __name__ == "__main__":
	root = Tk()
	root.title('Heart Animation')
	root.geometry('1000x600')
	app = Heart(root)
	app.mainloop()