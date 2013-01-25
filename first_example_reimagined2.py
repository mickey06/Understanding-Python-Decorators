from functools import wraps

def wrap_in_tag(tag):
    def factory(func):
        @wraps(func)
        def decorator(val):
            return func('<%(tag)s>%(val)s</%(tag)s>' %
                        {'tag': tag, 'val': val})
        return decorator
    return factory


@wrap_in_tag('b')
@wrap_in_tag('i')
def say(val):
    return val

say('hello')
print "with sugar"


say = wrap_in_tag('b')(wrap_in_tag('i')(say)))
print "No sugar"