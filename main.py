from window import Window
from point import Point
from line import Line


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

    window.wait_for_close()

main()