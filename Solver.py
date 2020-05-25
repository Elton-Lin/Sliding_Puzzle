import copy
from collections import deque
from enum import Enum
import heapq

import matrix



# https://www.redblobgames.com/pathfinding/a-star/implementation.html#algorithm
class PriorityQueue:
    def __init__(self):
        self.elements = []
        # another way to avoid same priority clashes:
        # add a counter into the tuple(after the weight) and count up when push()
    
    def empty(self):
        return len(self.elements) == 0
    
    def push(self, item, weight):
        # heapq sorts a tuple by starting at the first element, using '<'
        heapq.heappush(self.elements, (weight, item))
    
    def pop(self):
        # heapq defaults is a min-pq
        return heapq.heappop(self.elements)[1]



class Move(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    START = 4


class Node:

    def __init__(self, num_row: int, num_col: int, state: list, empty_pos: (int, int)):

        # turn 2d list to 1d? make it consistent

        self.num_row = num_row
        self.num_col = num_col
        self.state = state # 2D list representation of the board (e.g. [[0, 1], [2, 3]])
        self.prev_move = Move.START # previous node or/and move
        self.empty_pos = empty_pos


    # for comparing priority - arbitrary choice
    def __lt__(self, other):
        return True

    
    # retruns a list of nodes neighbored to itself
    def get_neighbors(self):

        # use own state and can move 
        nbs = []

        if self.can_move(0, 1):
            # print("moving left")
            new_node = self.get_new_node(0, 1)
            new_node.prev_move = Move.LEFT
            nbs.append(new_node)

        if self.can_move(0, -1):
            # print("moving right")
            new_node = self.get_new_node(0, -1)
            new_node.prev_move = Move.RIGHT
            nbs.append(new_node)
        
        if self.can_move(1, 0):
            # print("moving up")
            new_node = self.get_new_node(1, 0)
            new_node.prev_move = Move.UP
            nbs.append(new_node)
        
        if self.can_move(-1, 0):
            # print("moving down")
            new_node = self.get_new_node(-1, 0)
            new_node.prev_move = Move.DOWN
            nbs.append(new_node)

        return nbs


    def get_new_node(self, offset_row, offset_col):
        
        # offset = offset_row * self.num_col + offset_col
        # state = list(self.state)
        # cand = self.empty_pos + offset # the position to swap with
        # # print(offset, cand)
        # state[cand], state[self.empty_pos] = state[self.empty_pos], state[cand]

        # new_state = "".join(state)
        # new_node = Node(self.num_row, self.num_col, new_state, cand)

        r, c = self.empty_pos[0], self.empty_pos[1]
        new_r, new_c = r + offset_row, c + offset_col

        new_state = copy.deepcopy(self.state)
        new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
        new_node = Node(self.num_row, self.num_col, new_state, (new_r, new_c))

        # print("old", self.state)
        # print("new", new_state)

        return new_node



    def can_move(self, offset_row, offset_col):
        
        # coord = self.convert(self.empty_pos)
        # print(coord)
        # new_row = coord[0] + offset_row
        # new_col = coord[1] + offset_col

        new_row = self.empty_pos[0] + offset_row
        new_col = self.empty_pos[1] + offset_col

        if new_row >= 0 and new_row < self.num_row and\
           new_col >= 0 and new_col < self.num_col:
            return True
        else:
            return False


    # convert ordered number to grid coordinate
    # e.g. in a 2x2 matrix, convert(2) = (1, 0) because:
    # 0 1
    # 2 3
    def convert(self, pos):

        r = pos // self.num_col
        c = pos % self.num_col
        return (r, c)





class Solver:

    def __init__(self, board: list, num_row, num_col):

        self.board = board
        self.num_row = num_row
        self.num_col = num_col
        self.goal_state = []
        self.visited_states = {}


    def set_goal_and_find_empty(self):

        empty_pos = None

        for i in range(self.num_row):
            inner = []
            for j in range(self.num_col):
                inner.append(i * self.num_col + j)
                if self.board[i][j] == self.num_row * self.num_col - 1:
                    empty_pos = (i, j)
            self.goal_state.append(inner)

        return empty_pos



    def backtrack(self):

        solution_moves = []
        state = str(self.goal_state)
        while True:
            move, prev_state = self.visited_states[state]
            if move == Move.START:
                break
            solution_moves.append(move)
            state = prev_state

        return solution_moves 



    def Manhattan_heuristic(self, cur_state: list):

        distance = 0

        for row in range(self.num_row):
            for col in range(self.num_col):

                # conversion to find the goal(supposed) pose
                elem = cur_state[row][col]
                goal_row = elem // self.num_col
                goal_col = elem % self.num_col

                distance += (abs(row - goal_row) + abs(col - goal_col))

        return distance


    def a_star(self):

        start_state = self.board
        empty_pos = self.set_goal_and_find_empty()
        start_node = Node(self.num_row, self.num_col, start_state, empty_pos)

        frontier = PriorityQueue()
        cost_so_far = {}
        
        frontier.push(start_node, 0)
        cost_so_far[str(start_node.state)] = 0 # textbook g cost
        self.visited_states[str(start_node.state)] = (Move.START, "\0")

        while not frontier.empty():

            cur_node = frontier.pop()
            if cur_node.state == self.goal_state:
                print("goal!!!", cur_node.state)
                return self.backtrack()

            for nb in cur_node.get_neighbors():
                
                # print(nb.state)
                nb_state = str(nb.state)
                new_cost = cost_so_far[str(cur_node.state)] + 1 # every move cost 1

                # unvisited or have a lower cost
                # same node might be pushed twice, but it's fine because the lowest gets considered first
                if (nb_state not in self.visited_states) or (new_cost < cost_so_far[nb_state]):

                    cost_so_far[nb_state] = new_cost
                    self.visited_states[nb_state] = (nb.prev_move, str(cur_node.state))
                    priority = new_cost + self.Manhattan_heuristic(nb.state)
                    frontier.push(nb, priority)

                    # print(frontier.elements)

        print("no solution...")




    def bfs(self):

        start_state = self.board
        empty_pos = self.set_goal_and_find_empty()

        # empty = start_state.index(str(len(start_state) - 1))
        start_node = Node(self.num_row, self.num_col, start_state, empty_pos)
        
        # queue FIFO - append(right), popleft(left)
        node_queue = deque()
        node_queue.append(start_node)
        # external storage for tracking visited nodes
        self.visited_states[str(start_node.state)] = (Move.START, "\0")

        while len(node_queue) != 0:

            cur_node = node_queue.popleft()
            if cur_node.state == self.goal_state:
                print("goal!!!", cur_node.state)
                return self.backtrack()

            for nb in cur_node.get_neighbors():
                if str(nb.state) not in self.visited_states:
                    node_queue.append(nb)
                    self.visited_states[str(nb.state)] = (nb.prev_move, str(cur_node.state))
                    # print(nb.state)

        print("no solution...")




# puzzle = Mat.Matrix(3, 4)
# puzzle.print_grid()

# p = [[0, 1, 3, 2], [4, 9, 11, 7], [8, 5, 6, 10]]
# p = [[7, 4, 0], [1, 6, 8], [3, 5, 2]]

# p_solve = Solver(p, len(p), len(p[0]))
# print(p_solve.a_star())
# print(p_solve.bfs())
# print(p_solve.backtrack())

# p = [[1, 13, 2, 3], [0, 6, 9, 7], [4, 10, 11, 15], [12, 5, 8, 14]]
# p_solve = Solver(p, len(p), len(p[0]))
# print(p_solve.a_star())