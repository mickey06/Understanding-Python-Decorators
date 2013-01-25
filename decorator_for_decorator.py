# -*- coding: utf-8 -*-

# The decorator doesn't take args
#


def decorator1(f):
    def wrapper(arg1, arg2):
        return f(arg1, arg2)
    return wrapper


@decorator1
def function1(arg1, arg2):
    print("Hello", arg1, arg2)
#function1 = decorator1(function1)

function1("Universe and", "everything")

# The decorator takes args
#


def decorator_with_args(d):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(f):
            return d(f, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args
def decorator2(f, *args, **kwargs):
    def wrapper(arg1, arg2):
        return f(arg1, arg2)
    return wrapper
# decorator2 = decorator_with_args(decorator2)


@decorator2(42, 404, 1024)
def function2(arg1, arg2):
    print("Hello", arg1, arg2)
#function1 = decorator2(42, 404, 1024)(function2)

function2("Universe and", "everything")
