#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = "    " #difference between having outside of constructor and inside constructor?
                         #overriding attributes in base class?
    def __init__(self, content=None, **kwargs):
        self.content = []
        self.keyword_attributes = kwargs
        if content:
            self.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def build_tag(self):
        open_tag = '<{}'.format(self.tag)
        for key, value in self.keyword_attributes.items():
            open_tag += ' {}="{}"'.format(key,value)
        open_tag += '>'
        close_tag = '</{}>'.format(self.tag)
        return open_tag, close_tag

    def render(self, file_out, cur_ind=""):
        open_tag, close_tag = self.build_tag()
        file_out.write(cur_ind + open_tag + '\n')
        for html_content in self.content:
            if type(html_content) == str:
                file_out.write((cur_ind + "  ") + html_content +'\n')
            else:
                html_content.render(file_out, cur_ind + self.indent)
        file_out.write(cur_ind + close_tag + '\n')
            

class Html(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "html"
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind = ""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind)

class Body(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "body"
        super().__init__(content, **kwargs)

class P(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "p"
        super().__init__(content, **kwargs)

class Head(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "head"
        super().__init__(content, **kwargs)

class OneLineTag(Element):
    def __init__(self, content = None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind = ""):
        open_tag, close_tag = self.build_tag()
        file_out.write(cur_ind + open_tag)
        for html_content in self.content:
            if type(html_content) == str:
                file_out.write(html_content)
            else:
                html_content.render(file_out, self.indentation)
        file_out.write(close_tag + '\n')

class Title(OneLineTag):
    def __init__(self, content = None, **kwargs):
        self.tag = "title"
        super().__init__(content, **kwargs)

class SelfClosingTag(Element):
    def __init__(self,content = None, **kwargs):
        super().__init__(content, **kwargs)

    def append(self, content):
        if content:
            raise TypeError("Cannot add content to a Closing Tag.")

    def render(self, file_out, cur_ind = ""):
        file_out.write(cur_ind + self.tag + '\n')

class Hr(SelfClosingTag):
    def __init__(self, content = None, **kwargs):
        self.tag = "<hr />"
        super().__init__(content, **kwargs)


class Br(SelfClosingTag):
    def __init__(self, content = None, **kwargs):
        self.tag = "<br />"
        super().__init__(content, **kwargs)

class A(OneLineTag):
    def __init__(self, link = None, content = None):
        self.tag = "a"
        link_dict = {}
        link_dict['href'] = link
        super().__init__(content, **link_dict)

class Ul(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "ul"
        super().__init__(content, **kwargs)

class Li(Element):
    def __init__(self, content = None, **kwargs):
        self.tag = "li"
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, header_num = None, content = None, **kwargs):
        self.tag = "H" + str(header_num)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    def __init__(self, content = None, **kwargs):
        self.tag = "meta"
        super().__init__(content, **kwargs)

