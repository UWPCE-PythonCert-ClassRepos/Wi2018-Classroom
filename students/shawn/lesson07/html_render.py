from enum import Enum

class Tag:
    Open=1
    Close=2
    Span=3


class Element():

    def __init__(self,tag_type,markup=None,inline=None,val=None):
        self.tag_type=tag_type
        self.markup=markup
        self.inline=inline
        self.val=val

    def make_tag(self,indent=0):
        self.tag=""
        self.tag += f"<{ r'/' if self.tag_type==Tag.Close else ''}{self.markup}"
        if self.inline:
            self.tag += " style=\"" + self.inline + "\""
        if self.tag_type==Tag.Span:
            self.tag += f">{self.val}</{self.markup}>"
        else:
            self.tag += f">{self.val if self.val else ''}"
        return self.tag




class U_list(Element):

    def __init__(self,label,items):
        self.label=label
        self.items=items

    def make_list(self):
        self.ul = Element(Tag.Open,markup="ul",val=self.label + "\n").make_tag()
        self.ul += '\n'.join([Element(Tag.Span,markup="li",val=i).make_tag() for i in self.items])
        self.ul += Element(Tag.Close, markup="ul").make_tag()
        return self.ul





