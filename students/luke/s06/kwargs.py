#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs_lab.html#exercise-args-kwargs-lab
"""

def func(fore_color="black", back_color="white", link_color="blue", visited_color="red"):
    print(f"fore_color:\t{fore_color}")
    print(f"back_color:\t{back_color}")
    print(f"link_color:\t{link_color}")
    print(f"visited_color:\t{visited_color}")

def func2(*args):
    for arg in args:
        print(arg)


def func3(**kwargs):
    for arg in kwargs.keys():
        print(arg, kwargs[arg])


if __name__ == "__main__":
    func(link_color='red', back_color='blue')
    print()
    func2('red', 'blue', 'yellow', 'chartreuse')
    print()
    mydict = {'fore_color': 'purple', 'link_color': 'red', 'back_color': 'blue', 'visited_color': 'lilac'}
    func3(**mydict)
