import functools


def closure(message_one):

    def inner_function(num):
        for i in range(num):
            print(i)

    return inner_function


foo = closure("hi there")
bar = closure("snoo")
