# from tkinter import *

# master = Tk()

# master.geometry("200x200") 

# # to change text size, use font=("font name", size)
# w = Label(master, text="Hello, world!", font=("Helvetica", 22))

# # explicitly set the text to be at the top left corner
# w.place(anchor = NW, x = 0, y = 0)

# mainloop()

# from PIL import ImageTk, Image

# img = Image.open("images/hat.JPG")
# img.show()

# scale_width = scale_height = 8

# new_width = int(img.width // scale_width)
# new_height = int(img.height // scale_height)

# img = img.resize((new_width, new_height))
# img.show()


from PIL import Image, ImageOps
img = Image.open('images/hat.JPG')
img.show()
img2 = ImageOps.crop(img, border=20)
img_with_border = ImageOps.expand(img2,border=20) #fill='yellow'
img_with_border.show()

# img_with_border.save('imaged-with-border.png')