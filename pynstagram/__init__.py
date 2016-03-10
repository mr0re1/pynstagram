from pynstagram.client import PynstagramClient

__version__ = '0.1'


def client(*args, **kwargs):
    return PynstagramClient(*args, **kwargs)
