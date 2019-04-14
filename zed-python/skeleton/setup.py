try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My project for ex47',
    'author' : 'kaushik pal',
    'email' : 'kaushik853@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'ex47-lpthw'
}

setup(**config)

