#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    self.open_tag=''
    self.close_tag=''
    self.empty_tag=''

    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        self.content += new_content

    def render(self, file_out, cur_ind=""):
        self.content = self.open_tag + self.content + self.close_tag
        file_out.write(self.content)


class Html():
    def __init__(self):
        self.open_tag="<html>"
        self.close_tag="</html>"
        self.empty_tag="</>"
        super().__init__(content)


class Body(Element):
    def __init__(self):
        self.open_tag="<body>"
        self.close_tag="</body>"
        self.empty_tag="</>"
        super().__init__(content)


class P():
    def __init__(self):
        self.open_tag="<p>"
        self.close_tag="</p>"
        self.empty_tag="</>"
        super().__init__(content)
