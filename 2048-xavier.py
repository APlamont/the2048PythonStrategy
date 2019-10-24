"""
@file
@brief Simple strategy for 2048.
"""
import random
import numpy


class GameOverException(RuntimeError):
    """
    Raised when the game is over.
    """
    pass


class Game2048:
    """
    Implements the logic of the game :epkg:`2048`.
    """

    def __init__(self, game=None):
        """
        :param game: None or matrix 4x4
        """
        self.game = game or numpy.zeros((4, 4), dtype=int)
        self.moves = []

    def __str__(self):
        "Displays the game as a string."
        if len(self.moves) > 3:
            last_moves = self.moves[-3:]
        else:
            last_moves = self.moves
        return "{}\n{}".format(str(self.game), str(last_moves))

    def gameover(self):
        "Checks the game is over or not. Returns True in that case."
        return numpy.ma.masked_not_equal(self.game, 0).count() == 0

    def copy(self):
        "Makes a copy of the game."
        return Game2048(self.game.copy())

    def next_turn(self):
        "Adds a number in the game."
        if self.gameover():
            raise GameOverException("Game Over\n" + str(self.game))
        else:
            while True:
                i = random.randint(0, self.game.shape[0] - 1)
                j = random.randint(0, self.game.shape[1] - 1)
                if self.game[i, j] == 0:
                    n = random.randint(0, 3)
                    self.game[i, j] = 4 if n == 0 else 2
                    self.moves.append((i, j, self.game[i, j]))
                    break

    @staticmethod
    def process_line(line):
        """
        Moves numbers inside a vector whether this vector represents
        a row or a column.

        .. runpython::
            :showcode:

            from ensae_teaching_cs.td_1a.cp2048 import Game2048
            print(Game2048.process_line([0, 2, 2, 4]))
        """
        res = []
        for n in line:
            if n == 0:
                # Zero: skipped.
                continue
            if len(res) == 0:
                # First number: add.
                res.append(n)
            else:
                prev = res[-1]
                if prev == n:
                    # The number is identical: combine.
                    res[-1] = 2 * n
                else:
                    # Otherwise: add.
                    res.append(n)
        while len(res) < len(line):
            res.append(0)
        return res

    def play(self, direction):
        "Updates the game after a direction was chosen."
        if direction == 0: #gauche
            lines = [Game2048.process_line(self.game[i, :])
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 1: #haut
            lines = [Game2048.process_line(self.game[:, i])
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T
        elif direction == 2: #droite
            lines = [list(reversed(Game2048.process_line(self.game[i, ::-1])))
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 3: #bas
            lines = [list(reversed(Game2048.process_line(self.game[::-1, i])))
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T

    def score(self):
        "Returns the maximum values."
        return numpy.max(self.game)

    def best_move(self, game=None, moves=None):
        """
        Selects the best move knowing the current game.
        By default, selects a random direction.
        This function must not modify the game.

        @param  game        4x4 matrix or None for the current matrix
        @param  moves       all moves since the begining
        @return             one integer
        """
        if game is None:
            game = self.game
        if moves is None:
            moves = self.moves
        if moves is None:
            raise ValueError("moves cannot be None")
        if not isinstance(game, numpy.ndarray) or game.shape != (4, 4):
            raise ValueError("game must be a matrix (4x4).")
        return random.randint(0, 3)


def evaluate_strategy(fct_strategy, ntries=10):
    """
    Applies method *best_move* until gameover
    starting from the current position. Repeats *ntries* times
    and the maximum number in every try.

    @param      fct_strategy    a function which returns the best move
                                (see below)
    @return                     enumerator on scores

    One example to show how to test a strategy:

    .. runpython::
        :showcode:

        import random
        from ensae_teaching_cs.td_1a.cp2048 import evaluate_strategy

        def random_strategy(game, moves):
            return random.randint(0, 3)

        scores = list(evaluate_strategy(random_strategy))
        print(scores)
    """
    for i in range(0, ntries):
        g = Game2048()
        while True:
            try:
                g.next_turn()
            except (GameOverException, RuntimeError):
                break
            d = fct_strategy(g.game, g.moves)
            g.play(d)
        yield g.score()



import numpy
game = numpy.zeros((4, 4), dtype=int)

def indices_max(game):
    M = game.max()
    indices = []
    for i in range(4):
        for j in range(4):
            if game[i,j] == M:
                indices.append((i,j))
    return indices

def max_est_coin(game):
    for indice in indices_max(game):
        if indice in [(0,0), (0,3), (3,0), (3,3)]:
            return True
    return False

def nb_cases_vides(game):
    nb = 0
    for i in range(4):
        for j in range(4):
            if game[i,j] == 0:
                nb += 1
    return nb

def progressivite(game):
    scores = []
    for (i,j) in indices_max(game):
        #on étudie au dessus du max
        k = i
        score_haut = 0
        while k > 0 and game[k,j] == 2*game[k-1,j]:
            score_haut += 1
            k -= 1
        #on étudie en dessous du max
        k = i
        score_bas = 0
        while k < 3 and game[k,j] == 2*game[k+1,j]:
            score_bas += 1
            k += 1
        #on étudie à gauche du max
        k = j
        score_gauche = 0
        while k > 0 and game[i,k] == 2*game[i,k-1]:
            score_gauche += 1
            k -= 1
        #on étudie à droite du max
        k = j
        score_droite = 0
        while k < 3 and game[i,k] == 2*game[i,k+1]:
            score_droite += 1
            k += 1
        scores.append(max(score_haut, score_bas, score_gauche, score_droite))
    return max(scores)

def score(game):
    score = 0
    if max_est_coin(game):
        score += 25
    score += 3*nb_cases_vides(game)
    score += 1*progressivite(game)
    return score


#def strategy(game, moves=[]):
#    liste_scores = []
#    liste_case_max = []
#    est_meme = True
#    for direction in range(2):
#        g = Game2048()
#        g.game = game
#        g.play(direction)
#        est_meme = (not (game - g.game).any()) and est_meme
#        liste_scores.append(score(g.game))
#        liste_case_max.append(g.game.max())
#    if est_meme:
#        g = Game2048()
#        g.game = game
#        g.play(2)
#        est_meme = (not (game - g.game).any()) and est_meme
#        if not est_meme:
#            return 2
#        else:
#            return 3
#    M = max(liste_scores)
#    indices_max = []
#    for i in range(2):
#        if liste_scores[i] == M:
#            indices_max.append(i)
#    if len(indices_max) > 1:
#        return liste_case_max.index(max(liste_case_max))
#    else:
#        return indices_max[0]

def strategy(game, moves=[]):
    L = strategy2_aux(game)
    max = 0
    imax = 0
    for i in range(len(L)):
        if L[i][1] > max:
            max = L[i][1]
            imax = i
    return L[imax][0][0]

def aux(game, prof=3):
    if prof == 0:
        return []
    liste_finale = []

    for direction1 in range(4):
        g = Game2048()
        g.game = game
        g.play(direction)
        score1 = score(g.game)
        sum_score = score1

        for direction2 in range(4):
            g = Game2048()
            g.game = game
            g.play(direction2)
            score2 = score(g.game)
            sum_score += score2

            for direction3 in range(4):
                g = Game2048()
                g.game = game
                g.play(direction3)
                score3 = score(g.game)
                sum_score += score3

                liste_finale.append([[direction1, direction2, direction3], sum_score])
                sum_score = sum_score - score3

        sum_score = sum_score - score2

    sum_score = sum_score - score1

    return liste_finale

def strategy2_aux(game, moves=[]):
    game_ans = game.copy()
    L = [[[i,j,k],0] for i in range(4) for j in range(4) for k in range(4)]
    for index in range(len(L)):
        somme_score = 0
        [[i,j,k], _] = L[index]
        g = Game2048()
        g.game = game
        g.play(i)
        if (game_ans - g.game).any():
            somme_score += score(g.game)
            game_ans = g.game.copy()
            g.play(j)
            if (game_ans - g.game).any():
                somme_score += score(g.game)
                game_ans = g.game.copy()
                g.play(k)
                if (game_ans - g.game).any():
                    somme_score += score(g.game)
        L[index][1] = somme_score
    return L