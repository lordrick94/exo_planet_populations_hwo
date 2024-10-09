# Standard imports
import glob, os
from setuptools import setup, find_packages


# Begin setup
setup_keywords = dict()
setup_keywords['name'] = 'hwo_project'
setup_keywords['description'] = 'Simulation of Exoplanet observations for Habitable Worlds Observatory'
setup_keywords['author'] = 'L. Kahinga'
setup_keywords['author_email'] = 'lkahinga@ucsc.edu'
setup_keywords['license'] = 'GPLv3'
setup_keywords['url'] = 'git@github.com:lordrick94/exo_planet_populations_hwo.git'
setup_keywords['version'] = '0.1.dev0'
# Use README.rst as long_description.
setup_keywords['long_description'] = ''
if os.path.exists('README.md'):
    with open('README.md') as readme:
        setup_keywords['long_description'] = readme.read()
setup_keywords['provides'] = [setup_keywords['name']]
setup_keywords['requires'] = ['Python (>3.12.0)']
setup_keywords['install_requires'] = ['numpy', 'pyongc','astropy','pandas','matplotlib','scipy']

setup_keywords['zip_safe'] = False
setup_keywords['use_2to3'] = False
setup_keywords['packages'] = find_packages()
setup_keywords['setup_requires'] = ['pytest-runner']
setup_keywords['tests_require'] = ['pytest']

if os.path.isdir('bin'):
    setup_keywords['scripts'] = [fname for fname in glob.glob(os.path.join('bin', '*'))
                                 if not os.path.basename(fname).endswith('.rst')]

setup(**setup_keywords)
