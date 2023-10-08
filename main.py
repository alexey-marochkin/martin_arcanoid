from tkinter import *

root = Tk()
root.title("Markonoid")
root.geometry("800x600")
 
x = 375
y = 500 
mx = -10
my = -10

canvas = Canvas(bg="black", width=800, height=600)
canvas.pack(anchor=CENTER, expand=1)
ov = canvas.create_oval(x, y, x + 50, y + 50, width=2, outline="red")

def main():
    ball()
    root.after(20, main)

def ball():
    global mx, my
    canvas.move(ov, mx, my)
    x1, y1, x2, y2 = canvas.coords(ov)
    if (mx < 0 and x1 <= 0) or (mx > 0 and x2 >= 800):
        mx = mx * -1
    if (my < 0 and y1 <= 0) or (my > 0 and y2 >= 600):
        my = my * -1    
        

main()

root.mainloop()




