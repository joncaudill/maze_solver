from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    window = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    line = Line(point1, point2)
    window.draw_line(line, "red")
    point1_1 = Point(200, 200)
    point2_1 = Point(300, 300)
    line_1 = Line(point1_1, point2_1)
    window.draw_line(line_1, "blue")
    cell1 = Cell(100, 100, 200, 200, window)
    cell1.draw()
    cell2 = Cell(200, 200, 300, 300, window, has_left=False)
    cell2.draw()
    cell3 = Cell(300, 300, 400, 400, window, has_top=False)
    cell3.draw()
    cell4 = Cell(400, 400, 500, 500, window, has_right=False)
    cell4.draw()
    cell5 = Cell(500, 500, 600, 600, window, has_bottom=False)
    cell5.draw()
    cell6 = Cell(400, 100, 500, 200, window, has_top=False, has_bottom=False)
    cell6.draw()

    window.wait_for_close()

main()