'''
break_me.py
2018-01-24
KMG

Script to initiate four most common Python exceptions:
NameError
TypeError
SyntaxError
AttributeError
'''


def raiseNameError():
    try:
        print(a)

    except Exception as e: print(type(e).__name__)


def raiseTypeError():
    try:
        a = "Hello, world!"
        print(a+1)

    except Exception as e:print(type(e).__name__)


def raiseAttributeError():
    try:
        a = 1
        print(a.length)

    except Exception as e:print(type(e).__name__)


raiseNameError()
raiseTypeError()
raiseAttributeError()


# syntaxError fatal--add to end
# if True print("Hello, world!")
