#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    ### hints:
    ### there is a reason why it is not a string
    ### string may not be the best way to keep the content until rendered
    ### append function should just append
    open_tag=u''
    close_tag=u''
    empty_tag=u''

    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        try:
            self.content += new_content
        except TypeError:
            import pdb; pdb.set_trace()
            print('debug')


    def render(self, file_out, cur_ind=""):
        """ cur_ind should be the number of lines to indent """
        self.content = self.open_tag + self.content + self.close_tag
        file_out.write(self.content)


class Html():
    def __init__(self, content=None):
        self.open_tag="<html>"
        self.close_tag="</html>"
        self.empty_tag="</>"
        super().__init__(content)


class Body(Element):
    def __init__(self, content=None):
        self.open_tag="<body>"
        self.close_tag="</body>"
        self.empty_tag="</>"
        super().__init__(content)


class P():
    def __init__(self, content=None):
        self.open_tag="<p>"
        self.close_tag="</p>"
        self.empty_tag="</>"
        super().__init__(content)
