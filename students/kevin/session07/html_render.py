#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        self.content += new_content

    def render(self, file_out, cur_ind=""):
        file_out.write(self.content)

        
# NOTE: need "object" in Python2!
class Html(object):

    def __init__(self, content=None):
        pass


class Body():


class P():
