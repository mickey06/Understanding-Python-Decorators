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
