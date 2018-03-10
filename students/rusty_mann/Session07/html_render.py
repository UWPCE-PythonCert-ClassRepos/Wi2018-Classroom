#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
A class-based system for rendering html.
"""

# This is the framework for the base class


class Element(object):
    open_tag = ''
    close_tag = ''
    empty_tag = ''

    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        '''should only append'''
        self.content = list(content)
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, file_out, cur_ind=""):
        self.content = self.open_tag + self.content + self.close_tag
        #import pdb; pdb.set_trace()
        file_out.write(self.content)


class TextWrapper:
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


class Html(Element):
    def __init__(self, content=None):
        self.open_tag = "<html>"
        self.close_tag = "<html/>"
        super().__init__(content)


class Body(Element):
    def __init__(self, content=None):
        self.open_tag = "<body>"
        self.close_tag = "<body/>"
        super().__init__(content)


class P(Element):
    def __init__(self, content=None):
        self.open_tag = "<p>"
        self.close_tag = "<p/>"
        super().__init__(content)


