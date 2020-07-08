from setuptools import setup
from setuptools import find_packages

setup(
    name='movie-review-plus-package',
    version='0.0.1',
    description='Process peoples review and classify as Positive or Negative',
    author='Igor Souza',
    url='https://igormcsouza.github.io',
    install_requires=[
        'numpy', 
        'keras', 
        'nltk>=3.5', 
        'tqdm>=4.47.0',
        'matplotlib',
        'seaborn>=0.10.1'
    ],
    packages=find_packages()
)
