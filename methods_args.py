# -*- coding: utf-8 -*-


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 5  # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self, age):
        self.age = age

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)

l = Lucy(32)
l.sayYourAge(-3)
#outputs: I am 24, what did you think?
