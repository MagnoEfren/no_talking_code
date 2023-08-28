# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Canvas, Tk, Frame
from math import cos, sin 
from random import randint, choice


class Heart(Frame):
	def __init__(self, master):
		super().__init__(master)

		self.canvas = Canvas(master, bg = 'black')
		self.canvas.place(relx = 0, rely = 0, relwidth = 1, relheight=1)


		self.objects = []
		self.num = 0
		self.chars = ['➤', '♥', '☆','◉','➹','☼','❋','☺','♪']
		self.char = '☆'

		self.create_obj()
		self.update()

	def create_obj(self):
		for i in range(200):
			obj = self.canvas.create_text(0,0, font= ('Arial',24))
			self.canvas.coords(obj, 500, 250)
			self.objects.append(obj)

	def draw(self, obj, x,y, color, char):
		self.canvas.itemconfig(obj, fill = color, text=char)
		self.canvas.move(obj, x,y)

	def update(self):
		for t in range(0,200,1):
			xp = -1*int(16*pow(sin(t),3))
			yp = -1*int(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))
			color = '#{:02x}{:02x}{:02x}'.format(randint(100,255),0, randint(100,255))

			self.draw(self.objects[self.num], xp, yp, color, self.char)

			xy = self.canvas.coords(self.objects[self.num])

			self.num +=1
			if self.num >=200:
				self.num = 0 
			if xy[0]>=800:
				self.char = choice(self.chars)
				for s in range(200):
					self.canvas.moveto(self.objects[s], 520, 270)

		self.master.after(100, self.update)
if __name__ == '__main__':
	root =Tk()
	root.title('Heart Animation')
	root.geometry('1200x700')
	app = Heart(root)
	app.mainloop()
