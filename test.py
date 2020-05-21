# import tkinter as tk
# from PIL import ImageTk, Image


# img_src = Image.open("car.jpg")
# img_list = []

# # assign images to a list
# def partition(num_row, num_col):

#     # deal with precission and rounding error later
#     width = img_src.width // num_col
#     height = img_src.height // num_row
#     for i in range(num_row):
#         for j in range(num_col):
#             coord = (j * width, i * height, (j + 1) * width, (i + 1) * height)
#             # print(coord)
#             block = img_src.crop(coord)
#             img_list.append(block)

# partition(3, 4)
# for b in img_list:
#     b.show()

# https://stackoverflow.com/questions/41576637/are-rgba-pngs-unsupported-in-python-3-5-pillow
from PIL import Image

def flattenAlpha(img):
    alpha = img.split()[-1]  # Pull off the alpha layer
    ab = alpha.tobytes()  # Original 8-bit alpha

    checked = []  # Create a new array to store the cleaned up alpha layer bytes

    # Walk through all pixels and set them either to 0 for transparent or 255 for opaque fancy pants
    transparent = 50  # change to suit your tolerance for what is and is not transparent

    p = 0
    for pixel in range(0, len(ab)):
        if ab[pixel] < transparent:
            checked.append(0)  # Transparent
        else:
            checked.append(255)  # Opaque
        p += 1

    mask = Image.frombytes('L', img.size, bytes(checked))

    img.putalpha(mask)

    return img

# Run this as a test case.
# Assumes that you have a PNG named "CuriosityRover.png"
# that is an RGBA with varying levels of Alpha in the
# subdirectory assets from your working directory

if __name__ == "__main__":
    from PIL import ImageTk
    import tkinter as tk

    img = Image.open("images/mickey_mouse.png")
    img2 = Image.open("images/avatar.png")

    print(img.mode, img2.mode)

    # img = flattenAlpha(img)
    # img = img.convert("RGB")
    root = tk.Tk()

    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=600, height=600)

    canvas.create_image((300, 300), image=photo)
    canvas.grid(row=0, column=0)

    

    root.mainloop()


    



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