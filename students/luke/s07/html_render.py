#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = ''


    def __init__(self, content=None, style=None):
        self.content = []
        self.style = None
        if content:
            self.content.append(content) # string or Element
        if style:
            self.style = style


    def append(self, new_content):
        """ Take string or Element and append to our content"""
        self.content.append(new_content)


    def render(self, file_out, indent, depth=0):
        if self.tag:
            file_out.write(indent * depth + f"<{self.tag}")
            if self.style:
                file_out.write(f" {self.style}")
            file_out.write(f">\n")
        for element in self.content:
            if hasattr(element, 'render'):
                element.render(file_out, indent, depth + 1)
            else:
                file_out.write(indent * (depth + 1) + element + "\n")
        if self.tag:
            file_out.write(indent * depth + f"</{self.tag}>\n")


class Body(Element):
    tag = "body"


class Head(Element):
    tag = "head"


class Html(Element):
    tag = "html"


class P(Element):
    tag = "p"


class OneLineTag(Element):
    """ One-line HTML element with tags on same line """
    def render(self, file_out, indent, depth=0):
        file_out.write(indent * depth +
                       f"<{self.tag}>{self.content}</{self.tag}>\n")

    
class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    """ Self-contained HTML element; tag only """
    def __init__(self, content=None):
        if content:
            raise TypeError
        super().__init__()


    def render(self, file_out, indent, depth=0):
        file_out.write(indent * depth + f"<{self.tag} />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    def __init__(self, link, content):
        super().__init__(f"<a href={link}>{content}</a>")
