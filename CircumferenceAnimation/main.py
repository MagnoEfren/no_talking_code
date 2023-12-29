

from tkinter import Tk, Frame, Canvas
import numpy as np 
import colorsys 
class Animation(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.d = 2
        self.angle = 360 
        self.n = np.arange(1000)
        self.r = np.zeros(1000)
        self.phi = self.r 
        self.x =  self.r 
        self.y = self.r 
        self.dot = 1000*[0]
        self.color = 0 
        self.canvas = Canvas(master, bg= 'black')
        self.canvas.place(relx =0, rely = 0, relwidth =1, relheight=1)
        for i in self.n:
            self.dot[i] = self.canvas.create_rectangle(0,0,0,0)
        self.update()

    def update(self):
        self.angle += 0.0001
        self.color += 0.01 
        c = colorsys.hsv_to_rgb(self.color, 1, 1)
        color = '#{:02x}{:02x}{:02x}'.format(int(c[0]*255),
            int(c[1]*255),int(c[2]*255))
        if self.color >=1:
            self.color = 0 
        self.phi = self.angle*self.n 
        self.r = 10*np.sqrt(self.n)
        self.x = self.r*np.cos(self.phi)+400
        self.y = self.r*np.sin(self.phi)+350
        for i in self.n:
            self.canvas.coords(self.dot[i], self.x[i]-self.d,
                self.y[i]- self.d, self.x[i]+self.d, self.y[i]+ self.d)
            self.canvas.itemconfig(self.dot[i], outline= color, fill = color)
        self.after(10, self.update)
if __name__ == "__main__":
    root = Tk()
    root.title('Animation')
    root.geometry('800x800')
    app = Animation(root)
    app.mainloop()
