import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].has_bottom)

    def test_maze_reset_cells_visit(self):
        num_cols = 12
        num_rows = 10
        all_clear = True
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visit()
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j].visited:
                    all_clear = False
        self.assertTrue(all_clear)


if __name__ == "__main__":
    unittest.main()