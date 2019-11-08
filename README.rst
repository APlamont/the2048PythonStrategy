the2048PythonStrategy
===========

The 2048 game implemented with a solving strategy.
One example of use : 
`plot_strategy.py
<https://github.com/APlamont/2048/blob/master/examples/plot_strategy.py>`_.

Generate the setup in subfolder ``dist``:

::

    python setup.py sdist


Run the unit tests:

::

    python -m unittest discover tests

    
To check style:

::

    python -m flake8 pystrat2048 tests examples
