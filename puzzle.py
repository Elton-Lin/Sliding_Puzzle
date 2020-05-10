import tkinter as tk
from PIL import ImageTk, Image
import Matrix as mat


class Game(tk.Tk):

    # avoid logic in constructor, use another function
    def __init__(self, num_row, num_col):

        tk.Tk.__init__(self)

        # backend grid setup
        self.num_row = num_row
        self.num_col = num_col
        self.board = mat.Matrix(num_row, num_col)
        self.board.print_grid()

        # most important variable
        # positioin of the only empty block
        self.empty_pos = self.num_row * self.num_col - 1
        self.num_incorrect = 0

        # tkinter canvas setup
        self.canv = tk.Canvas(self, width=720, height=720)

        # pack and grid are geometric managers
        # self.canv.grid(row = 3, col = 3)
        self.canv.pack(fill="both", expand=True)

        # image setup
        self.img_src = Image.open("m5.jpg")
        # for saving img objects references, otherwise, it won't be displayed on tk
        self.cropped_imgs = []
        self.blocks = []

        self.block_width = 0
        self.block_height = 0


        # self.img = ImageTk.PhotoImage(Image.open("blue_square.png"))
        # self.block = self.canv.create_image(20, 20, anchor='nw', image=self.img)

        # cropped_img = self.img_src.crop((0,0,50,50))
        # self.tk_img = ImageTk.PhotoImage(cropped_img)
        # self.block2 = self.canv.create_image(20, 20, anchor='nw', image=self.tk_img)
        
        self.bind("<Key>", self.move_block)

        self.image_processing()


    def image_processing(self):

        # might also need resizing

        # partition image and assign each cropped images to list
        # deal with precission and rounding error later
        self.block_width = self.img_src.width // self.num_col
        self.block_height = self.img_src.height // self.num_row

        for i in range(self.num_row):
            for j in range(self.num_col):

                # omit the last block (right corner)
                if i == self.num_row - 1 and j == self.num_col - 1:
                    break

                coord = (j * self.block_width, i * self.block_height,\
                        (j + 1) * self.block_width, (i + 1) * self.block_height)
                print(coord)

                cropped_img = self.img_src.crop(coord)
                tk_img = ImageTk.PhotoImage(cropped_img)
                self.cropped_imgs.append(tk_img)

                block = self.canv.create_image(coord[0], coord[1], anchor='nw', image=tk_img)
                self.blocks.append(block)
                


    # fix variables names
    def update_board(self, offset):

        moving_block_pos = self.empty_pos + offset
        moving_elem = self.board.get_element(moving_block_pos)

        # every move of a block has 3 different results
        # - block moves from
        # 1. incorrect position into correct position
        # 2. incorrect position into another incorrect position
        # 3. correct position into incorrect position
        # (correct position is unique)

        # no
        if moving_elem != moving_block_pos:
            if moving_elem == self.empty_pos: # 1.
                self.num_incorrect -= 1
            else: # 2.
                pass
        else: # 3.
            self.num_incorrect += 1

        self.board.swap(moving_block_pos, self.empty_pos)
        self.empty_pos = moving_block_pos



    def can_move(self, offset_row, offset_col):
        
        # print("checking", self.empty_pos)
        coord = self.board.convert(self.empty_pos)
        # print("coord:", coord[0], coord[1])

        new_row = coord[0] + offset_row
        new_col = coord[1] + offset_col

        if new_row >= 0 and new_row < num_row and\
           new_col >= 0 and new_col < num_col:
            return True
        else:
            return False



    def move_block(self, event):

        key = event.keysym
        if key == "Left":
            # self.canv.move(self.block, -20, 0)   

            if self.can_move(0, 1):

                # move the block in display
                index = self.board.get_element(self.empty_pos + 1)
                self.canv.move(self.blocks[index], -1 * self.block_width, 0)
                # calculate offset: left, right (+-1), up, down (+- width)
                self.update_board(1)
                
                
            

        elif key == "Right":
            # self.canv.move(self.block, 20, 0)
            
            if self.can_move(0, -1):
                
                index = self.board.get_element(self.empty_pos - 1)
                self.canv.move(self.blocks[index], self.block_width, 0)
                self.update_board(-1)
                # print("empty pos:", self.empty_pos)
                # self.canv.move(self.blocks[self.empty_pos], self.block_width, 0)
                # print("empty pos after:", self.empty_pos)   

        elif key == "Up":
            # self.canv.move(self.block, 0, -20)

            if self.can_move(1, 0):
                index = self.board.get_element(self.empty_pos + self.num_col)
                self.canv.move(self.blocks[index], 0, -1 * self.block_height)
                self.update_board(self.num_col)

        elif key == "Down":
            # self.canv.move(self.block, 0, 20)

            if self.can_move(-1, 0):
                index = self.board.get_element(self.empty_pos - self.num_col)
                self.canv.move(self.blocks[index], 0, self.block_height)
                self.update_board(-1 * self.num_col)
        
        self.board.print_grid()
        print("number of incorrect blocks:", self.num_incorrect)


    # testing purposes
    def draw_rect(self):

        self.canv.create_rectangle(20, 20, 40, 40, fill='red')


if __name__ == '__main__':

    # input image
    # input dimensions: num_row, num_col (r*c)

    # image processing - crop image and store as blocks
    # pass blocks to game for display and animation
    
    num_row = 4
    num_col = 3

    game = Game(num_row, num_col)
    c = 0
    while True:
        game.update_idletasks()
        game.update()

        # if c > 10000:
        #     game.draw_rect()
        c += 1

    print("hi")
    