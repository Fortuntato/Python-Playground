#A context manager example

from contextlib import contextmanager

#decorator that adds enter and exit methods for the context manager
@contextmanager
def context_manager(obj):
    try:
        obj.some_property += 1
        yield   
    finally:
        obj.some_property -= 1

class an_object(object):
    def __init__(self,arg):
        self.some_property = arg