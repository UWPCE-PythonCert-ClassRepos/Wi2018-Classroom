#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    # The tag should be a class attr not an instance attr, according to Hettinger
    # And we need our tag to be html for the 1st test, 
    # the tag gets overwritten in subclasses
    tag = "html>"
    def __init__(self, content=None, style=""):
        if content:
            self.content = [content] # A list!
        else: 
            self.content = []
        if len(style)>1:
            self.style=style

    def append(self, new_content):
        self.content.append(new_content)

    # Ideally cur_ind = "" when initially calling render
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind+"<" + self.tag + "\n")

        for item in self.content:
            if type(item)== type("s"):
                file_out.write(cur_ind + "\t" + item + '\n')
            else: #Recursing cause I was told to.
                item.render(file_out, cur_ind+"\t")
        file_out.write(cur_ind + '</' + self.tag + '\n')


class Html(Element):
    # Kept the closing tags. It made sense at the time for some reason, but 
    # now it doesn't and I'm too lazy to refactor
    # But it looks like I'll need to to get style in there. ugh.
    tag = "html>"

class P(Element):
    tag = "p>"

class Body(Element):
    tag = "body>"

class Head(Element):
    tag = "head>"

class OneLineTag(Element):
    """
    Create a OneLineTag subclass of Element.
    It should override the render method, 
    to render everything 
    on 
    one 
    line
    """
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind+"<" + self.tag)
        for item in self.content:
            if type(item)== type("s"):
                file_out.write(" "+item+" ")
            else: 
                item.render(file_out, cur_ind+"\t")
        file_out.write('</' + self.tag + '\n')



class Title(OneLineTag):
    tag = "title>"
