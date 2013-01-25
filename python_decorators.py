"""

Very lightly modified from :
http://www.artima.com/weblogs/viewpost.jsp?thread=240808
http://www.artima.com/weblogs/viewpost.jsp?thread=240845

"""

# -*- coding: utf-8 -*-

print '-' * 5, "functions as decoration mechanisms", '-' * 5

print '>' * 2, "Decoration Setup for decorator with no args"


def entry_exit(f):
    print "Start wrapping :", f.__name__

    def wrap():
        print "Inside wrap before calling", f.__name__
        f()
        print "Inside wrap after calling", f.__name__
    print "End wrapping :", f.__name__
    return wrap


def func1():
    print "Inside func1()"
func1 = entry_exit(func1)
print "Wrap without decorator syntactic sugar entry_exit"


@entry_exit
def func2():
    print "Inside func2()"
print "Wrap with decorator syntactic sugar entry_exit"

print '>' * 2, "Start function calls"

func1()
func2()
print "final func1.__name__ :", func1.__name__

print '-' * 79


print '>' * 2, "Decoration Setup for decorator with args"


def decorator_with_args(arg1, arg2, arg3):
    print "Starting decorator_with_args"

    def wrap(f):
        print "Starting wrap", f.__name__

        def wrapped_f(*args):
            print "Starting wrapped_f()"
            print "Decorator arguments:", arg1, arg2, arg3
            print "Before calling f(*args)"
            f(*args)
            print "After calling f(*args)"
            print "Ending wrapped_f :", f.__name__

        print "Ending wrap :", f.__name__
        return wrapped_f
    return wrap


def Hello1(a1, a2, a3, a4):
    print 'Hello1 arguments:', a1, a2, a3, a4
Hello1 = decorator_with_args("hello", "world", 42)(Hello1)
print "Wrap sugar decorator_with_args without syntactic sugar"


@decorator_with_args("hello", "world", 42)
def Hello2(a1, a2, a3, a4):
    print 'Hello2 arguments:', a1, a2, a3, a4
print "Wrap sugar decorator_with_args with syntactic sugar"

print '>' * 2, "Start function calls"


print "Preparing to call Hello1()"
Hello1("say", "hello", "argument", "list")
print "after first Hello1() call"
Hello1("a", "different", "set of", "arguments")
print "after second Hello1() call"
print '\n',
print "Preparing to call Hello2()"
Hello2("say", "hello", "argument", "list")
print "after first Hello2() call"
Hello2("a", "different", "set of", "arguments")
print "after second Hello2() call"

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
