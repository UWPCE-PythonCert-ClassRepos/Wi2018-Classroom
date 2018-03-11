#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
A class-based system for rendering html.
"""

# This is the framework for the base class


class TextWrapper:

    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


class Element(object):

    tag = 'html'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, content):
        '''should only append'''
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def make_tags(self):
        attrs = " '".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs:
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag

    def render(self, file_out, cur_ind=""):
        open_tag, close_tag = self.make_tags()
        file_out.write(cur_ind + open_tag + "\n")
        #file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        for stuff in self.content:
            stuff.render(file_out, cur_ind + self.indent)
            file_out.write("\n")
        file_out.write(cur_ind + close_tag)
        #file_out.write("{}</{}>".format(cur_ind, self.tag))


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write("{}<{}>".format(cur_ind, self.tag))
        for stuff in self.content:
            stuff.render(file_out)
        file_out.write("</{}>".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'



