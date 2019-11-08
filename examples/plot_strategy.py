"""
Tries the PPW strategy and shows the results
============================================

The following example runs the game 2048 and keeps
the highest number obtained for every try with PPW strategy.
"""
import numpy
import matplotlib.pyplot as plt

from the2048PythonStrategy.PPWStrategy import PPW_strategy
from the2048PythonStrategy import evaluate_strategy, Game2048

##############################
# The strategy :func:`PPW_strategy
# <the2048PythonStrategy.PPWStrategy.PPW_strategy>`
# Tries to choose the best direction.

gen = evaluate_strategy(PPW_strategy, 100)
res = list(gen)
res.sort()
print(res)

#########################################
# Finaly plots the gains obtained by the strategy.

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.bar(numpy.arange(len(res)), res, color="b",
	   label="PPW", width=0.4)
ax.set_title("Our strategy for 2048.")
ax.legend()

#########################################
# Now another strategy.
# This one tries every direction and chooses the direction
# which keeps the most empty cells.

def look_into_every_direction_choose_best(game, state, moves):
	"""
	The strategy tries every direction and chooses the direction
	which keeps the most empty cells.
	"""
	best = None
	bestd = None
	for d in range(0, 4):
		g = Game2048(game.copy())
		g.play(d)
		empty = numpy.sum(g.game.ravel() == 0)
		if best is None or empty > best:
			best = empty
			bestd = d
	return bestd


############################################
# Let's play 50 games.
gen2 = evaluate_strategy(look_into_every_direction_choose_best, 100)
res2 = list(gen2)
res2.sort()
print(res2)


#########################################
# Finaly plots the gains obtained by the three strategies.

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.bar(numpy.arange(len(res)), res, color="b",
	label="PPW", width=0.27)
ax.bar(numpy.arange(len(res2)) + 0.27, res2, color="orange",
	label="best_empty", width=0.27)
ax.set_title("Compares two strategies for 2048.")
ax.legend()
##########################
# PPW seems really better !
plt.show()
