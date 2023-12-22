from tkinter import *
from ball import *
import random

root = Tk()
root.title("Markonoid")
root.geometry("800x600")

ovals = [
    
         ["ov1", 50, 150, 100,  0.3, -0.3, "red"],
         ["ov2", 150, 376, 500, -0.6, -5, "blue"],
         ["ov3", 75, 500, 300, -5, -10, "green"],
         ["ov4", 90, 400, 200, -15, -10, "brown"],
         ["ov5", 25, 20, 80, -5, -10, "purple"],
         ["ov6", 35, 120, 180, -5, -10, "yellow"],
         ["ov7", 45, 220, 380, -5, -10, "magenta"]
         
         ]

   

     
canvas = Canvas(bg="black", width=800, height=600)
canvas.pack(anchor=CENTER, expand=1)

for ov in ovals:
    ov[0] = Ball(canvas, ov[1], ov[6], ov[2], ov[3], random.random(), random.random())

ballsController = Ball_controler(ovals)

def main():
    
    global ballsController

    for ov in ovals:
        ov[0].move()
        ballsController.check(ov)

    root.after(1, main)
   
main()

root.mainloop()