from tkinter import *

root = Tk()
root.title("Markonoid")
root.geometry("800x600")
 
x = 375
y = 500 
m = -10

canvas = Canvas(bg="black", width=800, height=600)
canvas.pack(anchor=CENTER, expand=1)
ov = canvas.create_oval(x, y, x + 50, y + 50, width=2, outline="red")

def main():
    ball()
    root.after(50, main)

def ball():
    global m
    canvas.move(ov, 0, m)
    x1, y1, x2, y2 = canvas.coords(ov)
    if (m < 0 and y1 <= 0) or (m > 0 and y2 >= 600):
        m = m * -1
        

main()

root.mainloop()




