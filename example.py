"""
Tries the PPW strategy and shows the results
============================================

The following example runs 100 times the game 2048 and keeps
the highest number obtained for every try with PPW strategy.
"""
import numpy
import matplotlib.pyplot as plt

from the2048PythonStrategy import PPW_strategy, evaluate_strategy

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
plt.show()
