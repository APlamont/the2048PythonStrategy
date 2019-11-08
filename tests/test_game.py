"""
Unit tests for ``random_strategy``.
"""
import unittest
import numpy
from the2048PythonStrategy.cp2048 import Game2048


class TestGame(unittest.TestCase):

    def test_game_play(self):
        mat = numpy.zeros((4, 4), dtype=numpy.int32)
        mat[1, 1] = 1
        g = Game2048(mat)
        g.play(0)
        self.assertEqual(g.game[1, 1], 0)
        self.assertEqual(g.game[1, 0], 1)
        self.assertEqual(g.game.ravel().sum(), 1)


if __name__ == '__main__':
    unittest.main()
