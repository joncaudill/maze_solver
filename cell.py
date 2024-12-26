from point import Point
from line import Line

class Cell():
    def __init__(self, x1, y1, x2, y2, win = None, has_left=True, has_right=True, has_top=True, has_bottom=True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        x1 = self._x1
        y1 = self._y1
        x2 = self._x2
        y2 = self._y2
        point1 = Point(x1, y1)
        point2 = Point(x2, y1)
        point3 = Point(x1, y2)
        point4 = Point(x2, y2)
        top = Line(point1, point2)
        right = Line(point2, point4)
        bottom = Line(point3, point4)
        left = Line(point1, point3)
        if self.has_left:
            self._win.draw_line(left, "black")
        else:
            self._win.draw_line(left, "#d9d9d9")
        if self.has_right:
            self._win.draw_line(right, "black")
        else:
            self._win.draw_line(right, "#d9d9d9")
        if self.has_top:
            self._win.draw_line(top, "black")
        else:
            self._win.draw_line(top, "#d9d9d9")
        if self.has_bottom:
            self._win.draw_line(bottom, "black")
        else:
            self._win.draw_line(bottom, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        mid_x1 = (self._x1 + self._x2) // 2
        mid_y1 = (self._y1 + self._y2) // 2
        mid_x2 = (to_cell._x1 + to_cell._x2) // 2
        mid_y2 = (to_cell._y1 + to_cell._y2) // 2
        point1 = Point(mid_x1, mid_y1)
        point2 = Point(mid_x2, mid_y2)
        move = Line(point1, point2)
        self._win.draw_line(move, color)
        