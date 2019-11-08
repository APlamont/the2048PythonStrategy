the2048PythonStrategy
===========

The 2048 game implemented with a solving strategy.
This work was achieved by Alix Plamont, Théo Portalier and Yohan Wlockzysiak.
One example of use : 
`plot_strategy.py
<https://github.com/APlamont/the2048PythonStrategy/blob/master/examples/plot_strategy.py>`_.

Generate the setup in subfolder ``dist``:

::

    python setup.py sdist


Run the unit tests:

::

    python -m unittest discover tests

    
To check style:

::

    python -m flake8 the2048PythonStrategy tests examples


To execute the exemple and judge the strategy (a six minute run) :

::

    python -m examples.plot_strategy.py
