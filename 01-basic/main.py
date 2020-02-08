from tree1.file1 import *

test_loop()
test_nested_class()

def test_conditional():
    foo = 1
    bar = 5

    if foo > 5 or bar >= 5:
        print('Expected message #1')

    if foo > 0 and bar >= -1:
        print('Expected message #2')

    if foo + bar * 2 < 6:
        print('UNEXPECTED message #1')

    else:
        print('Expected message #3')

    bar = 0
    if foo and not bar:
        print('Expected message #4')

    elif foo:
        print('UNEXPECTED message #2')

    else:
        print('UNEXPECTED message #3')

def test_exceptions():
    try:
        int('hello!')

    except TypeError:
        print('Caught TypeError')
        return False

    except ValueError:
        print('Caught ValueError')
        return True

    finally:
        print('This should be printed')

def test_finally():
    try:
        if True:
            return 1

    finally:
        print('This should be printed')

test_conditional()
test_exceptions()
test_finally()

def function(a, b, c='blah', *args, **kwargs):
    print(a, b, c, args, kwargs)

function(1, 2, d=19)
function(None, None, 'blah', 'extra 1', 'extra 2', hello='world')
try:
    function()

except:
    print('Expected exception raised')

else:
    print('Expected exception NOT raised')

try:
    function(1)

except:
    print('Expected exception raised')

else:
    print('Expected exception NOT raised')

try:
    function('a', 'b', 'c', a=1)

except:
    print('Expected exception raised')

else:
    print('Expected exception NOT raised')

class Klass:
    def __init__(self, a, b):
        print('Klass.__init__:', (a, b))

    def test_instancemethod(self, a, b):
        print('Klass.test_instancemethod:', (a, b))

    @classmethod
    def test_classmethod(cls):
        print('classmethod', cls)

    @staticmethod
    def test_staticmethod(arg):
        print('classmethod', arg)

k = Klass('lorem', 'ipsum')
k.test_instancemethod(0, 1)
k.test_classmethod()
k.test_staticmethod(8)

def test_while():
    num = 10
    l = []
    while num >= 0:
        l.append(num)
        num -= 1

    print(l)

test_while()
