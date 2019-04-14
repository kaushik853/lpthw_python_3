try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My project for ex46',
    'author' : 'kaushik pal',
    'email' : 'kaushik853@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex46'],
    'scripts' : [],
    'name' : 'ex46-lpthw'
}

setup(**config)

