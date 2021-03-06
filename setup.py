import os

from setuptools import setup, find_packages
from productionserver import __include_files__, __version__


setup(
    name='django-productionserver',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/BryanHurst/django-productionserver',
    license='',
    author='Bryan Hurst',
    author_email='bryan@newline.us',
    description='Runs a Django Project using CherryPy as the App Server and nginx as the Static Asset Server.',
    requires=['futures', 'cherrypy', 'django']
)
