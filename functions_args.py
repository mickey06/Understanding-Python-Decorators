# -*- coding: utf-8 -*-

print '-' * 5, "functions as decoration mechanisms", '-' * 5

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


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print "Do I have args?:"
        print args
        print kwargs
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print "Python is cool, no argument here."

function_with_no_argument()
#outputs
#Do I have args?:
#()
#{}
#Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print a, b, c

function_with_arguments(1,2,3)
#outputs
#Do I have args?:
#(1, 2, 3)
#{}
#1 2 3
