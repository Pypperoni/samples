import sys

'''
$ python main.py nocatch
Traceback (most recent call last):
  File "main.py", line ?, in <module>
    test()
  File "main.py", line ?, in test_nocatch
    this_will_raise()
  File "main.py", line ?, in this_will_raise
    raise ValueError
ValueError

$ python main.py catch
$ python main.py catchall
$ python main.py catchother
Traceback (most recent call last):
  File "main.py", line ?, in <module>
    test()
  File "main.py", line ?, in test_catchother
    this_will_raise()
  File "main.py", line ?, in this_will_raise
    raise ValueError
ValueError

$ python main.py reraise
Traceback (most recent call last):
  File "main.py", line ?, in <module>
    test()
  File "main.py", line ?, in test_reraise
    this_will_raise()
  File "main.py", line ?, in this_will_raise
    raise ValueError
ValueError

$ python main.py catchandraise
Traceback (most recent call last):
  File "main.py", line ?, in <module>
    test()
  File "main.py", line ?, in test_catchandraise
    this_will_raise()
  File "main.py", line ?, in this_will_raise
    raise ValueError
ValueError

$ python main.py raiseother
Traceback (most recent call last):
  File "main.py", line ?, in <module>
    test()
  File "main.py", line ?, in test_raiseother
    raise TypeError
TypeError
'''

def this_will_raise():
    raise ValueError

def test_nocatch():
    this_will_raise()

def test_catch():
    try:
        this_will_raise()

    except Exception:
        pass

def test_catchall():
    try:
        this_will_raise()

    except:
        pass

def test_catchother():
    try:
        this_will_raise()

    except TypeError:
        pass

def test_reraise():
    try:
        this_will_raise()

    except:
        raise

def test_catchandraise():
    try:
        this_will_raise()

    except Exception as e:
        from __pypperoni__ import describeException
        print(describeException())
        raise

def test_raiseother():
    try:
        this_will_raise()

    except:
        raise TypeError

test = locals().get('test_' + sys.argv[1])
if not test:
    print('Unknown method', sys.argv[1])
    sys.exit(1)

test()
