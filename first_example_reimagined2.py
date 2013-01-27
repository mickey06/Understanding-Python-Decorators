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


class style(object):
  def __init__(self, tag):
    self.tag = tag
  def __call__(self, f):
    def newf(*args):
      return "<{tag}>{res}</{tag}>".format(res=f(*args), tag=self.tag)
    return newf


@style('b')
@style('i')
def say(val):
  return str(val)

