#!/usr/bin/env python3

class Element:
    open_tag = ''
    close_tag = ''

    def __init__(self, content=None):
        self.content = content or ''

    def append(self, new_content):
        if isinstance(new_content, Element):
            self.content += new_content
        else:
            print("Didn't work.")

    def render(self, file_out, cur_ind=''):
        self.content = self.open_tag + self.content + self.close_tag
        file_out.write(self.content)


class Html(Element):

    def __init__(self, content=None):
        self.open_tag = '<html>'
        self.close_tag = '</html>'
        Element.__init__(self, content)


class Body(Element):

    def __init__(self, content=None):
        self.open_tag = '<body>'
        self.close_tag = '</body>'
        Element.__init__(self, content)


class P(Element):

    def __init__(self, content=None):
        self.open_tag = '<p>'
        self.close_tag = '</p>'
        Element.__init__(self, content)

    #def __repr__(self):
        #return f'{self.open_tag}{self.close_tag}'
