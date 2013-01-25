# -*- coding: utf-8 -*-

print '-' * 5, "classes as decoration mechanisms", '-' * 5

print '>' * 2, "Decoration Setup for Class decorator with args"


class decorator_with_args(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print "Inside __call__()"

        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f


@decorator_with_args("hello", "world", 42)
def say_hello_1(a1, a2, a3, a4):
    print 'say_hello_1 arguments:', a1, a2, a3, a4
print "Use sugar"


def say_hello_2(a1, a2, a3, a4):
    print 'say_hello_2 arguments:', a1, a2, a3, a4
say_hello_2 = decorator_with_args("hello", "world", 42)(say_hello_2)
print "No sugar"

print '>' * 2, "End of Decoration Setup for Class decorator with args"

print "Preparing to call say_hello_1()"
say_hello_1("say", "hello", "argument", "list")
print "after first say_hello_1() call"
say_hello_1("a", "different", "set of", "arguments")
print "after second say_hello_1() call"

print "Preparing to call say_hello_2()"
say_hello_2("say", "hello", "argument", "list")
print "after first say_hello_2() call"
say_hello_2("a", "different", "set of", "arguments")
print "after second say_hello_2() call"
