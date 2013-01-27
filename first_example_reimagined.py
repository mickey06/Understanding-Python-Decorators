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

#
# Or using classes as the decorator mechanism
#


class b(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<b>{}</b>".format(self.f())


class i(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<i>{}</i>".format(self.f())


@b
@i
def sayhi():
    return 'hi'

#
# More flexibly
#


class sty(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, f):
        def newf():
            return "<{tag}>{res}</{tag}>".format(res=f(), tag=self.tag)
        return newf


@sty('b')
@sty('i')
def sayhi():
    return 'hi'
