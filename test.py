import tkinter as tk
from PIL import ImageTk, Image


img_src = Image.open("car.jpg")
img_list = []

# assign images to a list
def partition(num_row, num_col):

    # deal with precission and rounding error later
    width = img_src.width // num_col
    height = img_src.height // num_row
    for i in range(num_row):
        for j in range(num_col):
            coord = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            # print(coord)
            block = img_src.crop(coord)
            img_list.append(block)

partition(3, 4)
for b in img_list:
    b.show()


    



# img_src = Image.open("car.jpg")

# left = img_src.crop((0, 0, img_src.width // 2, img_src.height))
# right = img_src.crop((img_src.width // 2, 0, img_src.width, img_src.height))

# left.show()
# right.show()


# def func(event):
#     key = event.keysym
#     if key == "Left":
#         canv.move(blue, -20, 0)   
#     elif key == "Right":
#         canv.move(blue, 20, 0)
        
# root = tk.Tk()

# canv = tk.Canvas(root, width=800, height=800, bg='white')
# canv.grid(row=2, column=3)

# img = ImageTk.PhotoImage(Image.open("blue_square.png"))  # PIL solution
# blue = canv.create_image(20, 20, anchor='nw', image=img)
# root.bind("<Key>", func)

 



# tk.mainloop()