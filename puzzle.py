import tkinter as tk
from PIL import ImageTk, Image
import Matrix as mat


class Game(tk.Tk):


    def __init__(self):

        tk.Tk.__init__(self)

        # backend grid setup
        self.board = mat.Matrix(3, 3)
        self.board.print_grid()

        # most important variable
        self.empty_pos = 8 # positioin of the only empty block
        self.offset = 0

        # tkinter canvas setup
        self.canv = tk.Canvas(self, width=200, height=200)

        # pack and grid are geometric managers
        # self.canv.grid(row = 3, col = 3)
        self.canv.pack(fill="both", expand=True)

        self.img_src = ImageTk.PhotoImage(Image.open("blue_square.png"))
        self.block = self.canv.create_image(20, 20, anchor='nw', image=self.img_src)
        
        self.bind("<Key>", self.move_block)


    # fix variables names
    def update_board(self, offset):

        moving_block_pos = self.empty_pos + offset
        moving_elem = self.board.get_element(moving_block_pos)

        # no
        if moving_elem != moving_block_pos:
            if moving_elem == self.empty_pos: # no to yes
                self.offset += 1
            else: # no to no
                pass
        else: # yes to no
            self.offset -= 1

        self.board.swap(moving_block_pos, self.empty_pos)
        self.empty_pos = moving_block_pos



    def move_block(self, event):

        key = event.keysym
        if key == "Left":
            self.canv.move(self.block, -20, 0)     

            # can_move()
            # calculate offset: left, right (+-1), up, down (+- width)
            self.update_board(1)
            

        elif key == "Right":
            self.canv.move(self.block, 20, 0)
            
            self.update_board(-1)

        elif key == "Up":
            self.canv.move(self.block, 0, -20)

            self.update_board(3)

        elif key == "Down":
            self.canv.move(self.block, 0, 20)

            self.update_board(-3)
        
        self.board.print_grid()
        print("offset:", self.offset)


    # testing purposes
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
    