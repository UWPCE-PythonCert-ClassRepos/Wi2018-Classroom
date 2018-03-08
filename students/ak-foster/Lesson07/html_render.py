#!/usr/bin/env python3

class Element:
    open_tag = []
    close_tag = []

    def __init__(self, content=None):
        self.content = content or []

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):

        self.content = str(self.open_tag) + str(self.content) + str(self.close_tag)

        file_out.write(self.content)


class Html(Element):

    def __init__(self, content=None):
        self.open_tag = '<html>'
        self.close_tag = '</html>'
        super().__init__(content)

class Body(Element):

    def __init__(self, content=None):
        self.open_tag = '<body>'
        self.close_tag = '</body>'
        super().__init__(content)

class P(Element):

    def __init__(self, content=None):
        self.open_tag = '<p>'
        self.close_tag = '</p>'
        super().__init__(content)
