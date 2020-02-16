from tkinter import *

window=Tk()
#window.geometry("640x400+100+100")
#window.resizable(False,False)

canvas=Canvas(window,relief="groove",bd=2)

line=canvas.create_line(100,100,200,200,fill="red")
#polygon=canvas.create_polygon(50,50,170,170,100,170,outline="yellow")
arc=canvas.create_arc(100,100,200,200,start=10,extent=180)
canvas.pack()
