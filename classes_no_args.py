# -*- coding: utf-8 -*-

print '-' * 5, "classes as decoration mechanisms", '-' * 5
print '>' * 2, "Decoration Setup for Class decorator without args"


class decorator_no_args(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print "Inside __init__()"
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print "Inside __call__()"
        self.f(*args)
        print "After self.f(*args)"


@decorator_no_args
def say_hello_1(a1, a2, a3, a4):
    print 'say_hello_1 arguments:', a1, a2, a3, a4
print "Using sugar"


def say_hello_2(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4
say_hello_2 = decorator_no_args(say_hello_2)
print "Without sugar"

print "End of decoration Setup for Class decorator without args"

print "Preparing to call say_hello_1()"
say_hello_1("say", "hello", "argument", "list")
print "After first say_hello_1() call"
say_hello_1("a", "different", "set of", "arguments")
print "After second say_hello_1() call"

print "Preparing to call say_hello_2()"
say_hello_2("say", "hello", "argument", "list")
print "After first say_hello_2() call"
say_hello_2("a", "different", "set of", "arguments")
print "After second say_hello_2() call"