# I've removed calls for these functions. To test, call them yourself :)

def name_error():
    a = b


def type_error():
    x = "hello"
    y = x + 3


def syntax_error():
    haha {= 0


def attribute_error():
    y = name_error.thing
