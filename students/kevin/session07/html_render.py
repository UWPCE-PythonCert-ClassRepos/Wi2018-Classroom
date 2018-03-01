#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
# NOTE: need "object" in Python2!
class Element(object):
    open_tag = ''
    close_tag = ''
    empty_tag = ''
    
    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        try:
            self.content += new_content
        except TypeError:
            # import pdb; pdb.set_trace()
            # print('ok')

    def render(self, file_out, cur_ind=""):
        self.content = self.open_tag + self.content + self.close_tag
        file_out.write(self.content)

        
class Html(Element):
    # Will override parent class's __init__
    def __init__(self, content=None):
        self.open_tag = "<html>"
        self.close_tag = "</html>"
        super().__init__(content)


class Body(Element):
    def __init__(self, content=None):
        self.open_tag = "<body>"
        self.close_tag = "</body>"
        super().__init__(content)


class P(Element):
    def __init__(self, content=None):
        self.open_tag = "<p>"
        self.close_tag = "</p>"
        super().__init__(content)
    
