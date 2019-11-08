"""
Implements the PPW (Plamont Portalier Wloczysiak) strategy for the game 2048.
"""
from .cp2048 import Game2048


def indices_max(game):
    """
    Renvoie la liste des indices des cases dont la valeur est maximale.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
    M = game.max()
    indices = []
    for i in range(4):
        for j in range(4):
            if game[i,j] == M:
                indices.append((i,j))
    return indices


def max_est_coin(game):
    """
    Détermine (renvoie un booléen) si l'une des cases de valeur maximale
    est située dans un coin de la grille.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
    for indice in indices_max(game):
        if indice in [(0,0), (0,3), (3,0), (3,3)]:
            return True
    return False


def nb_cases_vides(game):
    """
    Renvoie le nombre de cases vides dans la grille.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
    nb = 0
    for i in range(4):
        for j in range(4):
            if game[i,j] == 0:
                nb += 1
    return nb


def progressivite(game):
    """
    Renvoie un score en fonction des schémas progressifs trouvés dans la grille,
    i.e. les séquences (2**1, 2**2, 2**3, ...) consécutives.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
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
    """
    Détermine le score d'une grille.
    Ce score représente le potentiel d'une grille pour les coups futurs.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
    coeffs = [256,128,16,3] #coefficients déterminés de façon
                            #à obtenir les meilleurs résultats
    score = 0
    if max_est_coin(game):
        score += coeffs[0]
    score += coeffs[1] * nb_cases_vides(game)
    score += coeffs[2] * progressivite(game)
    score += coeffs[3] * game.max()
    return score


def strategy_aux(game):
    """
    Renvoie la suite de trois coups consécutifs ayant le meilleur score.
	Le score d'une suite de trois coups est la somme des scores des 
	grilles obtenues en jouant ces trois coups.

    Paramètre game : matrice numpy 4x4 représentant la grille du jeu.
    """
    L = [[i,j,k] for i in range(4) for j in range(4) for k in range(4)]
    score_max = 0
    index_score_max = 0
    game_ans = game.copy()

    for index in range(len(L)):
        [i,j,k] = L[index]
        somme_score = 0 #somme des scores de chaque coup
        g = Game2048()
        g.game = game.copy()
        g.play(i)
        if (game_ans - g.game).any(): #si notre coup a pu être joué
            somme_score += score(g.game)
            game_ans = g.game.copy()
            g.play(j)
            if (game_ans - g.game).any():
                somme_score += score(g.game)
                game_ans = g.game.copy()
                g.play(k)
                if (game_ans - g.game).any():
                    somme_score += score(g.game)
        if somme_score > score_max:
            score_max = somme_score
            index_score_max = index
    return L[index_score_max]


def PPW_strategy(game, state=None, moves=None):
    """
    La strategie de résolution Plamont Portalier Wloczysiak
    détermine le coup à jouer à la date t à partir de l'état
    de la grille à la date t-1.
    Elle choisit pour cela le coup ayant le plus de potentiel
    pour l'avenir, i.e. le coup permettant de maximiser les
    scores des grilles futures sur trois coups.

    Paramètre game : matrice numpy 4x4 représentant la grille 
    du jeu à la date t-1.
    Paramètre state : stockage possible de tout ce dont on a 
    besoin (inutilisé).
    Paramètre moves : liste des coups précédents (inutilisé).

    Renvoie une direction dans {0,1,2,3}.
    """
    L = strategy_aux(game)
    return L[0]