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

        # Walk through content in the content list. If it's a string,
        # print it as content. Otherwise, we'll catch the TypeError
        # and treat it like another Element subclass and recursively
        # render it.
        print(tag_indent + self.open_tag())
        for item in self.content_items:
            try:
                print(content_indent + item)
            except TypeError:
                item.render(file_out, cur_ind+"    ")
        print(tag_indent + self.close_tag())

    def open_tag(self):
        return '<'+self.tag+'>'

    def close_tag(self):
        return '</'+self.tag+'>'


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"
