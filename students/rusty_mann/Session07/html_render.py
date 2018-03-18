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
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag

    def render(self, file_out, cur_ind=""):
        open_tag, close_tag = self.make_tags()
        file_out.write(cur_ind + open_tag + "\n")
#       file_out.write("{}<{}>\n".format(cur_ind, self.tag))
        for stuff in self.content:
            stuff.render(file_out, cur_ind + self.indent)
            file_out.write("\n")
        file_out.write(cur_ind + close_tag)
#       file_out.write("{}</{}>".format(cur_ind, self.tag))


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        open_tag, close_tag = self.make_tags()
        file_out.write(cur_ind + open_tag)
#        file_out.write("{}<{}>".format(cur_ind, self.tag))
        for stuff in self.content:
            stuff.render(file_out)
        file_out.write(close_tag)
#        file_out.write("</{}>".format(self.tag))


class SelfClosingTag(Element):
    """Base class for tags that have no content"""

    def append(self, *args, **kwargs):
        raise TypeError("content cannot be added to self closing tags")

    def render(self, file_out, cur_ind=""):

        open_tag, _ = self.make_tags()
        file_out.write(cur_ind + open_tag.replace(">", "/>"))


class Hr(SelfClosingTag):
    """Horizontal Rule"""

    tag = 'hr'


class Br(SelfClosingTag):
    """Line Break"""

    tag = 'br'


class Title(OneLineTag):
    """Title"""

    tag = 'title'


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind = cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class A(OneLineTag):
    """Anchor Element"""

    tag = "a"

    def __init__(self, link, *args, **kwargs):
        #how does this get run through make_tags()if it overwrites __init__ without creating self.attributes which is required for make_tags()
        kwargs['href'] = link
        super().__init__(*args, **kwargs)
        # this could also be direct:
        # Element.__init__(self, *args, **kwargs)


class Ul(Element):
    """Unordered List"""

    tag = "ul"


class Li(Element):
    """List Element"""

    tag = "li"


class H(OneLineTag):
    """Section Head"""

    tag = "h"

    def __init__(self, level, *args, **kwargs):
        self.tag += str(int(level))
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):
    """metatag tag"""

    tag = "meta"

