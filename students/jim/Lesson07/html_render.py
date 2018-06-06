#!/usr/bin/python3

class Element():
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.content_items = []
        self.attributes = {}
        if content is not None:
            self.content_items.append(content)
        for key, value in kwargs.items():
            self.attributes[key] = value

    def append(self, content):
        self.content_items.append(content)

    def render(self, file_out, cur_ind=""):
        # Set indents: content should be more indented than tags
        tag_indent = cur_ind
        content_indent = (cur_ind+"    ")

        print(tag_indent + self.open_tag())
        for item in self.content_items:
            if isinstance(item, str):
                print(content_indent + item)
            elif isinstance(item, Element):
                item.render(file_out, cur_ind+"    ")
            else:
                pass
        print(tag_indent + self.close_tag())

    def open_tag(self):
        ot = "<"+self.tag
        for key, value in self.attributes.items():
            ot += " "+str(key)+"="+str(value)
        ot += ">"
        return ot

    def close_tag(self):
        return '</'+self.tag+'>'


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        tag_indent = cur_ind
        content_indent = (cur_ind+"    ")

        line = self.open_tag() + " "
        for item in self.content_items:
            line += item + " "
        line += self.close_tag()
        print(line)


class Title(OneLineTag):
    tag = "title"
