#!/usr/bin/env python

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    open_tag = ""
    close_tag = ""
    content = ""

    def __init__(self, content = None):
        self.content = content '' #evaluating if something is true/false

    def append(self, new_content):
        try:
            self.content = new_content
        except: TypeError:
            import pdb;pdb.set_trace()
            print('ok')


    def render(self, file_out, cur_ind=""):
        self_content = self.open_tag + self.content + self.close_tag
        file_out.write(self_content)

class Html(Element): 
    def __init__(self):
        self.open_tag = "<html>"
        self.close_tag = "</html>"
        super().__init__(self, content = None) #same signature as parent

class Body(Element): #subclass
    def __init__(self):
        self.open_tag = "<body>"
        self.close_tag = "</body>"
        super().__init__(self, content = None)

class P(Element):
    def __init__(self):
            self.open_tag = "<p>"
            self.close_tag = "</p>"
            super().__init__(self, content = None)
    

