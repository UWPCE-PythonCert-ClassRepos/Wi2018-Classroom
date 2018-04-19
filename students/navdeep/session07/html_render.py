#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    open_tag = ''
    close_tag = ''
    indentation = "    "
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=""):
        format_html = ""
        for html_content in self.content:
            if type(html_content) == str:
                format_html = cur_ind + self.open_tag + '\n' + (cur_ind + "  ") + html_content +'\n' + cur_ind + self.close_tag +'\n'
            else:
                html_content.render(file_out, cur_ind + self.indentation)
            file_out.write(format_html)

class Html(Element):
    def __init__(self, content = None):
        self.open_tag = "<html>"
        self.close_tag = "</html>"
        self.indentation = ""
        super().__init__(content)

class Body(Element):
    def __init__(self, content = None):
        self.open_tag = "<body>"
        self.close_tag = "</body>"
        super().__init__(content)

class P(Element):
    def __init__(self, content = None):
        self.open_tag = "<p>"
        self.close_tag = "</p>"
        super().__init__(content)

class Head(Element):
    def __init__(self, content = None):
        self.open_tag = "<head>"
        self.close_tag = "</head>"
        super().__init__(content)

class OneLineTag(Element):
    def __init__(self, content = None):
        super().__init__(content)

    def render(self, file_out, cur_ind = ""):
        format_html = ""
        for html_content in self.content:
            if type(html_content) == str:
                format_html = cur_ind + self.open_tag  + html_content + self.close_tag + '\n'
            else:
                html_content.render(file_out, self.indentation)
            file_out.write(format_html)

class Title(OneLineTag):
    def __init__(self, content = None):
        self.open_tag = "<title>"
        self.close_tag = "</title>"
        super().__init__(content)
