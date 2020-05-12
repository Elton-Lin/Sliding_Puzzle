# from tkinter import *

# master = Tk()

# master.geometry("200x200") 

# # to change text size, use font=("font name", size)
# w = Label(master, text="Hello, world!", font=("Helvetica", 22))

# # explicitly set the text to be at the top left corner
# w.place(anchor = NW, x = 0, y = 0)

# mainloop()


# ---- resize -----
# from PIL import ImageTk, Image

# img = Image.open("images/hat.JPG")
# img.show()

# scale_width = scale_height = 8

# new_width = int(img.width // scale_width)
# new_height = int(img.height // scale_height)

# img = img.resize((new_width, new_height))
# img.show()

# ---- border -----
# from PIL import Image, ImageOps
# img = Image.open('images/hat.JPG')
# img.show()
# img2 = ImageOps.crop(img, border=20)
# img_with_border = ImageOps.expand(img2,border=20) #fill='yellow'
# img_with_border.show()

# img_with_border.save('imaged-with-border.png')


# ----- list of functions ----
# def add(x, y):
#     return x + y

# def minus(x, y):
#     return x - y

# funcs = [add, minus]
# print(funcs[0](2, 3))



# -------- button for shuffle -------
# from tkinter import *

# master = Tk()

# def callback():
#     print('click!')

# b = Button(master, text="OK", command=callback)
# b.pack()

# mainloop()


from tkinter import *
from PIL import ImageTk
import time

def scrollToTop(imaget):
    print("I'm in scrollToTop()")
    canvas.move(imaget, 0, -1)
    # t.after(1000, lambda:scrollToTop(imaget))

t = Tk()
canvas = Canvas(t,height=256,width=256)
canvas.pack()

arrows = [1]
arrows[0] = ImageTk.PhotoImage(file="images/blue_square.png")
image = canvas.create_image(20,100,image=arrows[0],tags="token")
t.mainloop()