import math
from tkinter import *

class Ball:
    def __init__(self, canvas: Canvas, diametr, color, x, y, dx=0.5, dy=0.5, printCoords=False):
        self.diametr = diametr
        self.radius = self.diametr/2
        self.printCoords = printCoords
        self.color = color
        self.stepX = dx
        self.stepY = dy
        self.x = x
        self.y = y
        self.canvasRight = 800
        self.canvasBottom = 600
        self.canvas = canvas
        self.oval = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x  + self.radius, self.y  + self.radius, width=2, outline = self.color, fill = self.color)
        self.vector = self.canvas.create_line(self.x, self.y, self.x + self.stepX, self.y + self.stepY, width = 7, fill="white", arrow=LAST)
        if printCoords:
            self.coordsText = canvas.create_text(self.x, self.y, font=("system", 6), fill = "white")

    def place(self):
        self.canvas.coords(self.oval, self.x, self.y)
        
    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.oval)

        self.x = x1 + self.radius
        self.y = y1 + self.radius

        if self.printCoords:
            self.canvas.itemconfigure(self.coordsText, text="x=%s y=%s" % (str(math.floor(self.x)), str(math.floor(self.y))))
            self.canvas.coords(self.coordsText, self.x, self.y)

        if (self.stepX < 0 and x1 <= 0) or (self.stepX > 0 and x2 >= self.canvasRight):
            self.stepX = self.stepX * -1

        if (self.stepY < 0 and y1 <= 0) or (self.stepY > 0 and y2 >= self.canvasBottom):
            self.stepY = self.stepY * -1   
        #-------------------------------------------------------------------------------
        
        c = self.radius / math.sqrt(self.stepX * self.stepX + self.stepY * self.stepY)
        self.canvas.coords(self.vector, self.x, self.y, self.x + self.stepX * c, self.y + self.stepY * c)
         
        self.canvas.move(self.oval,self.stepX,self.stepY)

class Ball_controler:

    def __init__(self, balls):
        self.balls = balls

    def check(self, ball):

        ov = ball    

        for nov in self.balls:
            if nov == ov:
                continue

            Dx = ov[0].x - nov[0].x
            Dy = ov[0].y - nov[0].y
            
            d = math.sqrt(Dx * Dx + Dy * Dy)
            if d == 0:
                d = 0.01

            s = Dx / d # sin
            e = Dy / d # cos

            if d < ov[0].radius + nov[0].radius:
                Vn1 = nov[0].stepX * s + nov[0].stepY * e
                Vn2 = ov[0].stepX * s + ov[0].stepY * e
                
                dt = (nov[0].radius + ov[0].radius - d) / (Vn1 - Vn2)
                
                if dt > 0.6: dt = 0.6
                if dt < -0.6: dt = -0.6

                ov[0].x -= ov[0].stepX * dt
                ov[0].y -= ov[0].stepY * dt
                nov[0].x -= nov[0].stepX * dt
                nov[0].y -= nov[0].stepY * dt

                Dx = ov[0].x - nov[0].x
                Dy = ov[0].y - nov[0].y
                d = math.sqrt(Dx * Dx + Dy * Dy)
                if d == 0: d = 0.01
                s = Dx / d # sin
                e = Dy / d # cos
                
                Vn1 = nov[0].stepX * s + nov[0].stepY * e
                Vn2 = ov[0].stepX * s + ov[0].stepY * e
                
                Vt1 = -nov[0].stepX * e + nov[0].stepY * s
                Vt2 = -ov[0].stepX * e + ov[0].stepY * s                

                o = Vn2
                Vn2 = Vn1
                Vn1 = o

                ov[0].stepX = Vn2 * s - Vt2 * e
                ov[0].stepY = Vn2 * e + Vt2 * s
                nov[0].stepX = Vn1 * s - Vt1 * e
                nov[0].stepY = Vn1 * e + Vt1 * s         

                ov[0].canvas.move(ov[0].oval, ov[0].stepX * dt, ov[0].stepY * dt)
                nov[0].canvas.move(nov[0].oval, nov[0].stepX * dt, nov[0].stepY * dt)
