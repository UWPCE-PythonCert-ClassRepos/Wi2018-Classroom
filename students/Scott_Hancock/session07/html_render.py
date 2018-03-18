#!/usr/bin/env python

"""
A class-based system for rendering html,
"""

class Element(object):
    open_tag = ''
    close_tag = ''

    def __init__(self, content=None, **attrs):
        self.content = content or ''
        self.attrs = attrs
        for key, value in self.attrs.items():
            self.open_tag = ''.join((self.open_tag, ' ', key, '=\"', value, '\"'))

    def append(self, new_content):
        if hasattr(new_content, 'outputResult'):
            self.content = self.content + new_content.outputResult('')
        else:
            self.content = self.content + str(new_content)

    def outputResult(self, cur_ind):
        return ''.join((cur_ind, '<', self.open_tag, '>', '\n', cur_ind, self.content, '\n', cur_ind, '</', self.close_tag, '>', '\n'))

    def render(self, file_out, cur_ind=''):
        file_out.write(self.outputResult(cur_ind))

class OneLineTag(Element):
    def outputResult(self, cur_ind):
        return ''.join((cur_ind, '<', self.open_tag, '>', self.content, '</', self.close_tag, '>', '\n'))

class SelfClosingTag(Element):
    def outputResult(self, cur_ind):
        return ''.join((cur_ind, '<', self.open_tag, ' />', '\n'))

class Title(OneLineTag):
    open_tag = 'title'
    close_tag = 'title'

class Ul(Element):
    open_tag = 'ul'
    close_tag = 'ul'

class Li(Element):
    open_tag = 'li'
    close_tag = 'li'

class P(Element):
    open_tag = 'p'
    close_tag = 'p'

class Meta(SelfClosingTag):
    open_tag = 'meta'
    close_tag = 'meta'

    def __init__(self, charset=None, content=None, **attrs):
        self.content = content or ''
        self.attrs = attrs
        self.attrs['charset'] = charset
        for key, value in self.attrs.items():
            self.open_tag = ''.join((self.open_tag, ' ', key, '=\"', value, '\"'))

class A(Element):
    open_tag = 'a'
    close_tag = 'a'

    def __init__(self, link=None, content=None, **attrs):
        self.content = content or ''
        self.attrs = attrs
        self.attrs['href'] = link
        for key, value in self.attrs.items():
            self.open_tag = ''.join((self.open_tag, ' ', key, '=\"', value, '\"'))

class H(OneLineTag):
    open_tag = 'h1'
    close_tag = 'h1'

    def __init__(self, level, content=None, **attrs):
        self.open_tag = 'h{:d}'.format(level)
        self.close_tag = 'h{:d}'.format(level)
        super(H, self).__init__(content, **attrs)

class Body(Element):
    open_tag = 'body'
    close_tag = 'body'

class Html(Element):
    open_tag = 'html'
    close_tag = 'html'

    def outputResult(self, cur_ind):
        return ''.join((cur_ind, '<!DOCTYPE html>\n', ''.join((super(Html, self).outputResult('')))))

class Head(Element):
    open_tag = 'head'
    close_tag = 'head'

class Hr(SelfClosingTag):
    open_tag = 'hr'

class Br(SelfClosingTag):
    open_tag = 'br'

my_instantiation = Element('hello')