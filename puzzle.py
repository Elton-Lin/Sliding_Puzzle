import tkinter as tk
from PIL import ImageTk, Image

class Game(tk.Tk):


    def __init__(self):

        tk.Tk.__init__(self)
        self.canv = tk.Canvas(self, width=200, height=200)

        # pack and grid are geometric managers
        # self.canv.grid(row = 3, col = 3)
        self.canv.pack(fill="both", expand=True)

        self.img_src = ImageTk.PhotoImage(Image.open("blue_square.png"))
        self.block = self.canv.create_image(20, 20, anchor='nw', image=self.img_src)
        
        self.bind("<Key>", self.move_block)


    def move_block(self, event):

        key = event.keysym
        if key == "Left":
            self.canv.move(self.block, -20, 0)        
        elif key == "Right":
            self.canv.move(self.block, 20, 0)    
        elif key == "Up":
            self.canv.move(self.block, 0, -20)        
        elif key == "Down":
            self.canv.move(self.block, 0, 20) 


    def draw_rect(self):

        self.canv.create_rectangle(20, 20, 40, 40, fill='red')


if __name__ == '__main__':

    # input image
    # input dimensions: num_row, num_col (r*c)

    # image processing - crop image and store as blocks
    # pass blocks to game for display and animation
    

    game = Game()
    c = 0
    while True:
        game.update_idletasks()
        game.update()

        # if c > 10000:
        #     game.draw_rect()
        c += 1

    print("hi")
    