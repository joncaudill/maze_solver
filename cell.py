from point import Point
from line import Line
from window import Window

class Cell():
    def __init__(self, x1, y1, x2, y2, win, has_left=True, has_right=True, has_top=True, has_bottom=True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom

    def draw(self):
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
        if self.has_right:
            self._win.draw_line(right, "black")
        if self.has_top:
            self._win.draw_line(top, "black")
        if self.has_bottom:
            self._win.draw_line(bottom, "black")