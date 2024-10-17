import tkinter as tk
import subprocess
from tkinter import PhotoImage
import os

def start():
    global root 
    root = tk.Tk()
    root.title('Sakha Your Mate')
    canvas = tk.Canvas(root, width=1200, height=781)
    canvas.grid(column=0, row=1)
    
    # Ensure the path is correct
    img_path = os.path.join("resources", "sakhaaa.png")
    img = PhotoImage(file=img_path)
    
    canvas.create_image(0, 0, image=img, anchor=tk.NW)

    root.after(3000, lambda: root.destroy())  # close the window after 3 seconds
    root.mainloop()

if __name__ == '__main__':
    start()
    subprocess.Popen(['python', 'scripts/link.py'])  # open link.py
