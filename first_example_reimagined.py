from functools import wraps

def wrap_in_tag(tag):
    def factory(func):
        @wraps(func)
        def decorator():
            return '<%(tag)s>%(rv)s</%(tag)s>' % (
                {'tag': tag, 'rv': func()})
        return decorator
    return factory


@wrap_in_tag('b')
@wrap_in_tag('i')
def say():
    return 'hello'

makebold = wrap_in_tag('b')
makeitalic = wrap_in_tag('i')

@makebold
@makeitalic
def say():
    return 'hello'