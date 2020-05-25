import Game
import sys

if __name__ == '__main__':
    
    print("what")

    # ----User input processing---
    if len(sys.argv) != 2:
        print("Exiting...\nUsage: python3 puzzle.py path_to_img")
        exit()

    img_path = sys.argv[1]

    print("Emter the dimensions to create a m x n puzzle")
    num_row = int(input("m (row): "))
    num_col = int(input("n (col): "))

    if num_row < 2 or num_col < 2:
        print("Puzzle size needs to be greater than 2 x 2")
        exit()


    game = Game.Game(num_row, num_col, img_path)
    game.pre_processing()
    game.mainloop()
    
    # mainloop() is equilvalent to this:
    # while True:
    #     game.update_idletasks()
    #     game.update()

    print("Game is exited")
    