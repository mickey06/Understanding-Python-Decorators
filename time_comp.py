# -*- coding: utf-8 -*-
import cProfile

def fm(f):
    def wrap():
        f()
    return wrap

class cm(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        self.f(*args)






