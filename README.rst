the2048PythonStrategy
===========

The 2048 game implemented with a solving strategy.

This work was achieved by `Alix Plamont
<https://github.com/APlamont>`_, `Théo Portalier
<https://github.com/tportalier>`_ and `Yohan Wloczysiak
<https://github.com/YohanWloczysiak>`_.

One example of use : 
`example.py
<https://github.com/APlamont/the2048PythonStrategy/blob/master/example.py>`_.

Generate the setup in subfolder ``dist``:

::

    python setup.py sdist


Run the unit tests:

::

    python -m unittest discover tests

    
To check style:

::

    python -m flake8 .


To execute the exemple and judge the strategy with 100 parties (a six minute run) :

::

    python example.py

The average 2048 rate is almost 7% with our strategy.
