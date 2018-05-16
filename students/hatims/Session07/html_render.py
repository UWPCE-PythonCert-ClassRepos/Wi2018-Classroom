#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    open_tag = "<html>"
    close_tag =  "</html>"
    def __init__(self, content=""):
        self.content = content
        self.store = []
        self.store.append(content)

    def append(self, new_content):
        self.store.append(new_content)

    def render(self, file_out, cur_ind=""):
        self.store.insert(0, self.open_tag)
        self.store.insert(len(self.store), self.close_tag)
        file_out.write(str(self.store))

class Html(Element):
    open_tag = "<html>"
    close_tag =  "</html>"
    #def __init__(self, content=""):
    #    self.content = content
    #    self.store = []				
    #    super(Html, self).__init__(self.content)

    #def append(self, new_content):
    #    self.store.append(new_content.content)
		
class Body(Element):
    open_tag = "<body>"
    close_tag = "</body>"
    #def __init__(self, content=""):
    #    self.content = content
    #    self.store = []		
    #    self.open_tag = "<body>"
    #    self.close_tag = "</body>"
    #    super(Body, self).__init__(self.content)
    #    #Element.append(self, self.content)
    #def append(self, new_content):
    #    self.store.append(new_content.content)
		
class P(Element):
    open_tag = "<p>"
    close_tag = "</p>"
    #def __init__(self, content=""):
    #    self.content = content	
    #    self.open_tag = "<p>"
    #    self.close_tag = "</p>"
    #    super(P, self).__init__(self.content)
    #    Element.append(self, self.open_tag + self.content + self.close_tag)
	