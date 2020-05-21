class Matrix:

    # grid is a 2D list (maybe should use an array)
    grid = []

    def __init__(self, height, width):

        self.height = height
        self.width = width
        self.fill_grid() # be optional?, user cast

    # fill the matrix with 0 to width * height - 1
    def fill_grid(self):

        for i in range(self.height):
            self.grid.append(list())
            for j in range(self.width):
                self.grid[i].append(i * self.width + j)
    
    def print_grid(self):

        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end = ' ')
            print('')


    def swap(self, pos1, pos2):

        p1 = self.convert(pos1)
        p2 = self.convert(pos2)
        # \ is a line break to allow a statement be on multiple lines
        self.grid[p1[0]][p1[1]], self.grid[p2[0]][p2[1]]\
        = self.grid[p2[0]][p2[1]], self.grid[p1[0]][p1[1]]


    # convert ordered number to grid coordinate
    def convert(self, pos):

        h = pos // self.width
        w = pos % self.width
        return (h, w)

    def get_element(self, pos):
        
        coord = self.convert(pos)
        return self.grid[coord[0]][coord[1]]


    # reset elements to be ordered
    def reset(self):
        
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = i * self.width + j


# test_b = Matrix(3, 4)
# # test_b.fill_grid()
# # test_b.print_grid()
# test_b.swap(2, 3)
# test_b.print_grid()

# print(test_b.get_element(7))
# print(test_b.get_element(2))
