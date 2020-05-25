import game
import sys

if __name__ == '__main__':
    
    print("Starting...")

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


    sliding_puzzle = game.Game(num_row, num_col, img_path)
    sliding_puzzle.pre_processing()
    sliding_puzzle.mainloop()
    
    # mainloop() is equilvalent to this:
    # while True:
    #     sliding_puzzle.update_idletasks()
    #     sliding_puzzle.update()

    print("Game is exited")
    