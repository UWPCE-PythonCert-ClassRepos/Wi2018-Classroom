class Element():

    def __init__(self, content=None):
        self.tag = "html"
        self.content_items = []
        if content is str:
            self.content_items.append(content)

    def append(self, content):
        self.content_items.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind+'<'+self.tag+'>'+"\n")
        for item in self.content_items:
            file_out.write(cur_ind+"  "+item+"\n")
        file_out.write(cur_ind+'</'+self.tag+'>')
