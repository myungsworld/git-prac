import time
from tkinter import *
window=Tk()

canvas=Canvas(window,width=400,height=200)
canvas.pack()

canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    canvas.move(1,5,2)
    window.update()
    time.sleep(0.05)
