# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Tk, Frame, Canvas
from math import cos, sin
from random import randint 

class Donut(Frame):
	def __init__(self, master):
		super().__init__(master)

		self.canvas = Canvas(master, bg = 'black')
		self.canvas.place(relx = 0, rely=0, relwidth = 1, relheight = 1)

		self.A = 0
		self.B = 0
		self.R1 = 10
		self.R2 = 30 
		self.K2 = 200 
		self.K1 = 40*self.K2*3/(8*(self.R1 + self.R2))
		self.objects = []
		self.num = 0 
		self.x = 0 
		self.y = 0 
		self.chars = '.,-~:;=!*#$@"'
		self.create_obj()
		self.update()


	def create_obj(self):
		for i in range(1600):
			obj = self.canvas.create_text(0, i, font=('Arial', 14))
			self.objects.append(obj)

	def draw(self, obj, char, x,y, color):
		self.canvas.itemconfig(obj, fill = color, text = char)
		self.canvas.coords(obj, 200+x, y)

	def update(self):
		output = [' ']*1600
		zbuffer = [0]*1600

		for theta in range(0, 628, 10 ):
			for phi in range(0, 628, 3):

				cosA = cos(self.A)
				sinA = sin(self.A)
				cosB = cos(self.B)
				sinB = sin(self.B)

				costheta = cos(theta)
				sintheta = sin(theta)
				cosphi = cos(phi)
				sinphi = sin(phi)

				circlex = self.R2 +self.R1*costheta
				circley = self.R1*sintheta

				x = circlex*(cosB*cosphi+sinA*sinB*sinphi)- circley*cosA*sinB
				y = circlex*(sinB*cosphi-sinA*cosB*sinphi)+ circley*cosA*cosB
				z = self.K2+ cosA*circlex*sinphi+circley*sinA
				inver_z = 1/z 

				xp = int(20+self.K1*inver_z*x)
				yp = int(20 - self.K1*inver_z*y)
				position = xp +40*yp 

				L = cosphi*costheta*sinB -cosA*costheta*sinphi -sinA*sintheta+ cosB*(
					cosA*sintheta-costheta*sinA*sinphi)
				if inver_z > zbuffer[position]:
					zbuffer[position] = inver_z
					index = int(L*8)
					output[position] = self.chars[index if index > 0 else 0 ]

		for i in range(40):
			self.y += 16
			for j in range(40):
				self.x += 16
				color = '#{:02x}{:02x}{:02x}'.format(randint(50,255), randint(50, 255), randint(50, 255))
				self.draw(self.objects[self.num], output[self.num], self.x, self.y, color)
				self.num += 1
			self.x = 0 
		self.y = 0 
		self.num = 0 
		self.A += 0.12
		self.B += 0.23 

		self.master.after(50, self.update)

if __name__ == '__main__':
	root = Tk()
	root.title('Donut Animation')
	root.geometry('1000x600')
	app = Donut(root)
	app.mainloop()
