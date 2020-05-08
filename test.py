import tkinter as tk
from PIL import ImageTk, Image

def func(event):
    key = event.keysym
    if key == "Left":
        canv.move(blue, -20, 0)   
    elif key == "Right":
        canv.move(blue, 20, 0)
        
root = tk.Tk()

canv = tk.Canvas(root, width=800, height=800, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("blue_square.png"))  # PIL solution
blue = canv.create_image(20, 20, anchor='nw', image=img)
root.bind("<Key>", func)

 



tk.mainloop()