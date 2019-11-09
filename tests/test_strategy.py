"""
Unit tests for ``PPW_strategy``.
"""
import unittest
import numpy
import random
from the2048PythonStrategy import PPW_strategy, evaluate_strategy


class TestStrategy(unittest.TestCase):

    def test_PPW_strategy(self):
        """
        Teste 10 fois, pour une grille de départ aléatoire,
        si la stratégie renvoie bien une direction correcte.
        """
        for i in range(10):
            L = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
            game = [random.choice(L) for _ in range(16)]
            game = numpy.array(game)
            game = game.reshape(4, 4)
            rnd = PPW_strategy(game)
            assert rnd in {0, 1, 2, 3}

    def test_measure_strategy(self):
        """
        Teste si la fonction d'évaluation de la stratégie
        renvoie bien une valeur strictement positive.
        """
        gen = evaluate_strategy(PPW_strategy)
        res = list(gen)
        assert isinstance(res, list)
        assert all(map(lambda x: x > 0, res))


if __name__ == '__main__':
    unittest.main()
