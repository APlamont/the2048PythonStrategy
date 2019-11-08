# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}

with open(os.path.join(here, "requirements.txt"), "r") as f:
    requirements = f.read().strip(' \n\r\t').split('\n')
if len(requirements) == 0 or requirements == ['']:
    requirements = []

setup(name='the2048PythonStrategy',
      version='0.1',
      description="Example of module to implement a strategy for 2048",
      long_description="Exemple de module python implémentant une "
                       "stratégie pour le jeu 2048",
      author='Alix Plamont, Théo Portalier et Yohan Wloczysiak',
      author_email='alix.plamont@ensae.fr ; theo.portalier@ensae.fr ; yohan.wloczysiak@ensae.fr',
      url='https://github.com/APlamont/the2048PythonStrategy',
      packages=packages,
      package_dir=package_dir,
      # requires indique quels packages doivent être installés
      # également pour que cela fonctionne
      requires=requirements)
