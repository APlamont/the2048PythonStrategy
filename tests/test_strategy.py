"""
Unit tests for ``PPW_strategy``.
"""
import unittest
import numpy
import random
from the2048PythonStrategy.PPWStrategy import PPW_strategy
from the2048PythonStrategy import evaluate_strategy


class TestStrategy(unittest.TestCase):

    def test_PPW_strategy(self):
        """
        Teste, pour une grille de départ aléatoire,
        si la stratégie renvoie bien une direction correcte.
        """
        for _ in range(10):
            game = numpy.array([random.choice([0, 2, 4, 8, 16, 32, 64,
                128, 256, 512, 1024]) for _ in range(16)])
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
