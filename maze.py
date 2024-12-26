import time
import random
from cell import Cell

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win = None,
                 seed = None):
        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visit()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + j * self._cell_size_x
                y1 = self._y1 + i * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _reset_cells_visit(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                

    def _draw_cell(self, i, j):
        x = self._x1 + j * self._cell_size_x
        y = self._y1 + i * self._cell_size_y
        x1 = x + self._cell_size_x
        y1 = y + self._cell_size_y
        cell = Cell(x, y, x1, y1, self._win)
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is not None:
            self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom = False
        self._cells[0][0].draw()
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()
        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            possible = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible.append("up")
                possible.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                possible.append("left")
                possible.append((i, j - 1))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible.append("down")
                possible.append((i + 1, j))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible.append("right")
                possible.append((i, j + 1))
            if possible == []:
                self._cells[i][j].draw()
                return
            direction = random.randrange(0, len(possible))
            match possible[direction]:
                case "left":
                    self._cells[i][j].has_left = False
                    self._cells[i][j - 1].has_right = False
                    to_visit.append((i, j - 1))
                    self._break_walls_r(i, j - 1)
                case "up":
                    self._cells[i][j].has_top = False
                    self._cells[i - 1][j].has_bottom = False
                    to_visit.append((i - 1, j))
                    self._break_walls_r(i - 1, j)
                case "right":
                    self._cells[i][j].has_right = False
                    self._cells[i][j + 1].has_left = False
                    to_visit.append((i, j + 1))
                    self._break_walls_r(i, j + 1)
                case "down":
                    self._cells[i][j].has_bottom = False
                    self._cells[i + 1][j].has_top = False
                    to_visit.append((i + 1, j))
                    self._break_walls_r(i + 1, j)
    
    def solve(self):
        solved = self._solve_r(0, 0)
        if solved:
            return True
        return False
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if i > 0 and not self._cells[i][j].has_top and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            success = self._solve_r(i - 1, j)
            if success:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        if j > 0 and not self._cells[i][j].has_left and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            success = self._solve_r(i, j - 1)
            if success:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        if i < self._num_cols - 1 and not self._cells[i][j].has_bottom and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            success = self._solve_r(i + 1, j)
            if success:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        if j < self._num_rows - 1 and not self._cells[i][j].has_right and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            success = self._solve_r(i, j + 1)
            if success:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False