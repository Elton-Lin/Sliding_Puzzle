import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image, ImageOps
import random as rand
import Matrix as mat
import time



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
        self.MAXSIZE = 760        

        # image setup
        self.img_src = Image.open("images/car.jpg")
        # for saving img objects references, otherwise, it won't be displayed on tk
        self.cropped_imgs = []
        self.blocks = []

        self.block_width = 0
        self.block_height = 0

        self.canv = None

        

        self.frame_buttons = tk.Frame()
        self.frame_buttons.grid(row = 0, column = 0, sticky = 'N')

        self.button_shuffle = tk.Button(self.frame_buttons, text = 'Shuffle', command = self.shuffle)
        self.button_restart = tk.Button(self.frame_buttons, text = 'Restart', command = self.restart)

        self.button_shuffle.pack()#grid(row = 0, column = 0, sticky = 'N')
        self.button_restart.pack()#grid(row = 0, column = 0)
        
        self.thumbnail = self.resize_img(self.MAXSIZE // 4)
        self.tk_thumb = ImageTk.PhotoImage(self.thumbnail)
        self.lab = tk.Label(image = self.tk_thumb)
        self.lab.grid(row = 0, column = 0, sticky = 'S')
        

        # unbind when doing shuffling?
        self.bind("<Key>", self.move_block)



    def resize_img(self, max_size):
        
        width = self.img_src.width
        height = self.img_src.height
        
        # rescale width and height with same value to keep image undistorted
        scale = max(width, height) // max_size
        new_width = int(width // scale)
        new_height = int(height // scale)

        return self.img_src.resize((new_width, new_height))



    # 1. Fix RGBA conditionally
    # 2. Resize image conditionally
    # 3. Canvas setup
    # 4. Image processing - ...
    def pre_processing(self):

        # might want to add the transparent RGBA conversion (flattenAlpha)

        # Resize to predetermined max size if img too large
        if max(self.img_src.width, self.img_src.height) > self.MAXSIZE:
            self.img_src = self.resize_img(self.MAXSIZE)

        # tkinter canvas setup
        # pack and grid are geometric managers
        self.canv = tk.Canvas(self, width=self.img_src.width, height=self.img_src.height)
        # self.canv.pack(fill="both", expand=True)
        self.canv.grid(row = 0, column = 1)

        self.image_processing()
        
        # create a button for shuffle instead
        # self.shuffle()
        
    # partition image and assign each cropped images as blocks to a list
    # draws the tk_image blocks on canvas        
    def image_processing(self):

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

                strip_border = ImageOps.crop(cropped_img, border=2)
                add_border = ImageOps.expand(strip_border, border=2)

                tk_img = ImageTk.PhotoImage(add_border)
                self.cropped_imgs.append(tk_img)

                block = self.canv.create_image(coord[0], coord[1], anchor='nw', image=tk_img)
                self.blocks.append(block)

        # self.canv.create_line([50, 50, 50, 150])

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


    def move_left(self):

        # move the block in display
        index = self.board.get_element(self.empty_pos + 1)
        self.canv.move(self.blocks[index], -1 * self.block_width, 0)
        # calculate offset: left, right (+-1), up, down (+- width)
        self.update_board(1)

    def move_right(self):

        index = self.board.get_element(self.empty_pos - 1)
        self.canv.move(self.blocks[index], self.block_width, 0)
        self.update_board(-1)

    def move_up(self):

        index = self.board.get_element(self.empty_pos + self.num_col)
        self.canv.move(self.blocks[index], 0, -1 * self.block_height)
        self.update_board(self.num_col)

    def move_down(self):

        index = self.board.get_element(self.empty_pos - self.num_col)
        self.canv.move(self.blocks[index], 0, self.block_height)
        self.update_board(-1 * self.num_col)


    def move_block(self, event):

        key = event.keysym
        if key == "Left":
            if self.can_move(0, 1):
                self.move_left()
                
        elif key == "Right":
            if self.can_move(0, -1):   
                self.move_right()

        elif key == "Up":
            if self.can_move(1, 0):
                self.move_up()

        elif key == "Down":
            if self.can_move(-1, 0):
                self.move_down()
        
        self.board.print_grid()
        print("number of incorrect blocks:", self.num_incorrect)

        if(self.num_incorrect == 0):
            tk.messagebox.showinfo("Game info", "Well done!")
            print("Done")


    def shuffle(self):
        
        self.button_restart['state'] = 'disabled'
        condition = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        moves = [self.move_left, self.move_right, self.move_up, self.move_down]

        num_shuffle = self.num_col * self.num_row * 4
        last_index = -1
        while num_shuffle > 0:

            index = rand.randrange(0, 4)
            # avoid moving opposite directions immediately
            if abs(index - last_index) == 1 and index + last_index != 3:
                continue
            
            (x, y) = condition[index]
            if(self.can_move(x, y)):
                
                moves[index]()
                self.update()
                time.sleep(0.2)
                last_index = index

            num_shuffle -= 1
        
        self.num_incorrect =  self.count_incorrect()
        self.button_restart['state'] = 'normal'



    def restart(self):
        
        # reset all blocks to its correct positions
        self.board.reset()
        self.board.print_grid()
        self.num_incorrect = 0
        self.empty_pos = self.num_col * self.num_row - 1

        index = 0
        for block in self.blocks:

            (row, col) = self.board.convert(index)
            pose = (col * self.block_width, row * self.block_height)
            self.canv.coords(block, pose)
            index += 1

        # self.update()
        # self.shuffle()


    def count_incorrect(self):

        index = 0
        counter = 0
        for i in range(self.num_row):
            for j in range(self.num_col):
                elem = self.board.grid[i][j]
                # avoid couting the empty block
                if  elem != index and elem != self.num_row * self.num_col - 1:
                    counter += 1
                index += 1

        return counter


    # testing purposes
    def draw_rect(self):

        self.canv.create_rectangle(20, 20, 40, 40, fill='red')


import sys

if __name__ == '__main__':

    # input image
    # input dimensions: num_row, num_col (r*c)

    # image processing - crop image and store as blocks
    # pass blocks to game for display and animation
    
    # ----User input processing---
    # if len(sys.argv) != 2:
    #     print("Exiting...\nUsage: python3 puzzle.py path_to_img")
    #     exit()

    # img_path = sys.argv[1]

    # print("Emter the dimensions to create a m x n puzzle")
    # num_row = int(input("m (row): "))
    # num_col = int(input("n (col): "))
    # if num_row < 2 or num_col < 2:
    #     print("Really? puzzle size needs to be greater than 2 x 2")
    #     exit()

    num_row = 4
    num_col = 3

    game = Game(num_row, num_col)
    game.pre_processing()
    game.mainloop()
    # c = 0
    # while True:
    #     game.update_idletasks()
    #     game.update()

    #     # if c > 10000:
    #     #     game.draw_rect()
    #     c += 1

    print("hi")
    