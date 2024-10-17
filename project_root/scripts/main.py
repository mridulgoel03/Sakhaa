import tkinter as tk
from tkinter import *
import random
import time
import subprocess

def start():
    global root 
    root = Tk()
    root.title('Sakha your mate')
    canvas = Canvas(root,width=1200,height=781)
    canvas.grid(column=0,row=1)
    img = PhotoImage(file="sakhaaa.png")
    canvas.create_image(0,0,image=img,anchor=NW)

    root.after(3000, lambda: root.destroy())  # close the window after 5 seconds

    root.mainloop()

if __name__=='__main__':
    start()
    subprocess.Popen(['python', 'link.py'])  # open the main.py file
