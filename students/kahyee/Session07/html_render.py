#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


# This is the framework for the base class
class Element(object):
    
    tag = 'html'
    indent = ' ' * 4
    
    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        try:
            self.content += new_content
        except TypeError:
            self.content += new_content.content

    def render(self, file_out, cur_ind=""):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        self.content = self.open_tag + self.content + self.close_tag
        file_out.write(self.content)

class Html(Element):
    
    self.tag = "html"
    
class Body(Element):
    
    self.tag = "body"

class P(Element):
    
    self.tag = "p"
