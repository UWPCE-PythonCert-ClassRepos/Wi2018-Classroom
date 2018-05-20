#!/usr/bin/env python
#!/usr/bin/env python3


"""
A class-based system for rendering html.
"""

class TextWrapper():
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


# This is the framework for the base class
class Element(object):
    
    tag = 'html'
    indent = ' ' * 4
    
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, file_out, cur_ind=""):
        attributes = ' '.join([' {}="{}"'.format(k, v) for k, v in self.attributes.items()])
        self.open_tag = '<' + self.tag + attributes + '>\n'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(cur_ind + self.open_tag)
        for element in self.content:
            element.render(file_out, cur_ind + self.indent)
            file_out.write("\n")
        file_out.write(cur_ind + self.close_tag)
        
class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        attributes = ' '.join([' {}="{}"'.format(k, v) for k, v in self.attributes.items()])
        self.open_tag = '<' + self.tag + attributes + '>'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(cur_ind + self.open_tag)
        for element in self.content:
            element.render(file_out)
        file_out.write(self.close_tag)
        
class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=""):
        attributes = ' '.join([' {}="{}"'.format(k, v) for k, v in self.attributes.items()])
        only_tag = '<' + self.tag + attributes + ' />'
        file_out.write(cur_ind + only_tag)
        
class A(Element):
    
    tag = "a"
    
    def __init__(self, link, content):
        Element.__init__(self, content, href = link)
        
class H(OneLineTag):
    
    tag = "h"
    
    def __init__(self, level, content):
        self.tag = "h" + str(level)
        super().__init__(content)
    

class Html(Element):
    
    tag = "html"
    
    def render(self, file_out, cur_ind=""):
        file_out.write('<DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind="")
    
class Body(Element):
    
    tag = "body"

class P(Element):
    
    tag = "p"

class Ul(Element):
    
    tag = "Ul"

class Li(Element):
    
    tag = "li"
    
class Head(Element):
    
    tag = "head"

class Title(OneLineTag):
    
    tag = "title"
    
    
class Hr(SelfClosingTag):
    
    tag = "hr"

class Br(SelfClosingTag):
    
    tag = "br"
    
class Meta(SelfClosingTag):
    
    tag = "meta"
    
    
