from tkinter import *

root = Tk()
root.title("Markonoid")
root.geometry("800x600")

ovals = [["ov1", 150, 100, -5, -20, "red"] , ["ov2", 375, 500, -10, -10, "blue"], ["ov3", 500, 300, -10, -10, "green"], ["ov4", 400, 200, -5, -10, "yellow"], ["ov5", 20, 80, -5, -10, "purple"]]

canvas = Canvas(bg="black", width=800, height=600)
canvas.pack(anchor=CENTER, expand=1)

for ov in ovals:
    ov[0] = canvas.create_oval(ov[1], ov[2], ov[1] + 50, ov[2] + 50, width=2, outline=ov[5], fill=ov[5])


def main():
    for ov in ovals:
        ov = ball(ov)

    root.after(50, main)

def ball(ov):
    # --------- oval -- mx----my----
    canvas.move(ov[0], ov[3], ov[4])
    x1, y1, x2, y2 = canvas.coords(ov[0])
    if (ov[3] < 0 and x1 <= 0) or (ov[3] > 0 and x2 >= 800):
        ov[3] = ov[3] * -1
    if (ov[4] < 0 and y1 <= 0) or (ov[4] > 0 and y2 >= 600):
        ov[4] = ov[4] * -1   
    return ov

 
        

main()

root.mainloop()




