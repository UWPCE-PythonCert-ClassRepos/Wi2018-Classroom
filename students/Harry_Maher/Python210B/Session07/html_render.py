#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class Element:
    # The tag should be a class attr not an instance attr
    # (according to Hettinger).
    # And we need our tag to be html for the 1st test,
    # the tag gets overwritten in subclasses
    tag = "html"
    
    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]  # A list!
        else:
            self.content = []


    def append(self, new_content):
        self.content.append(new_content)

    # Ideally cur_ind = "" when initially calling render
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<" + self.tag + ">\n")
        # Recursing cause I was told to.
        for item in self.content:
            if type(item) == type("s"):
                file_out.write(cur_ind + "\t" + item + '\n')
            else:
                item.render(file_out, cur_ind+"\t")
        file_out.write(cur_ind + '</' + self.tag + '>\n')


class Html(Element):
    tag = "html"


class P(Element):
    tag = "p"


class Body(Element):
    tag = "body"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    """
    Create a OneLineTag subclass of Element.
    It should override the render method,
    to render everything
    on
    one
    line
    """
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<" + self.tag + "> ")
        for item in self.content:
            if type(item) == type("s"):
                file_out.write(item)
            else:
                item.render(file_out, cur_ind+"\t")
        file_out.write(' </' + self.tag + '>\n')


class Title(OneLineTag):
    tag = "title"
