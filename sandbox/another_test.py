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


# from tkinter import *
# from PIL import ImageTk
# import time

# def scrollToTop(imaget):
#     print("I'm in scrollToTop()")
#     canvas.move(imaget, 0, -1)
#     # t.after(1000, lambda:scrollToTop(imaget))

# t = Tk()
# canvas = Canvas(t,height=256,width=256)
# canvas.pack()

# arrows = [1]
# arrows[0] = ImageTk.PhotoImage(file="images/blue_square.png")
# image = canvas.create_image(20,100,image=arrows[0],tags="token")
# t.mainloop()


# ------label buttons thumbnail---
# import tkinter as tk

# root = tk.Tk()

# l1 = tk.Label(root, text="hello")
# l2 = tk.Label(root, text="world")
# f1 = tk.Frame(root)
# b1 = tk.Button(f1, text="One button")
# b2 = tk.Button(f1, text="Another button")

# l1.grid(row=0, column=0)
# l2.grid(row=0, column=1)
# f1.grid(row=1, column=1, sticky="nsew")

# b1.pack(side="top")
# b2.pack(side="top")

# root.mainloop()




# impressive generic solvers!
# https://github.com/fabianokafor369/Sliding-puzzle-solver/blob/master/main.py (# pyhton2
# CARE! the empty block is 0 in this code)
# https://github.com/YahyaAlaaMassoud/Sliding-Puzzle-A-Star-Solver

# puzzle = [[1, 13, 2, 3], [0, 6, 9, 7], [4, 10, 11, 15], [12, 5, 8, 14]]


# cur_state = [[0, 1, 3, 2], [4, 9, 11, 7], [8, 5, 6, 10]]

# distance = 0

# for row in range(3):
#     for col in range(4):

#         # conversion to find the supposed pose
#         elem = cur_state[row][col]
#         goal_row = elem // 4
#         goal_col = elem % 4

#         distance += (abs(row - goal_row) + abs(col - goal_col))

# print(distance)

import heapq

# https://www.redblobgames.com/pathfinding/a-star/implementation.html#algorithm
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def push(self, item, weight):
        # heapq sorts a tuple by starting at the first element, using '<'
        heapq.heappush(self.elements, (weight, item))
    
    def pop(self):
        # heapq defaults is a min-pq
        return heapq.heappop(self.elements)[1]


class Blah:

    def __init__(self, s):
        self.s = s

pq = PriorityQueue()

b1 = Blah("hi")
b2 = Blah("hey")

pq.push(b1, 10)
pq.push(b2, 5)

print(pq.pop().s)
print(pq.pop().s)