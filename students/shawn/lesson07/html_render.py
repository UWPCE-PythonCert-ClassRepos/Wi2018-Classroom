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

    def add_spaces(self,spaces):
        return " " * spaces

    def make_tag(self,indent=0,is_break=True):
        self.tag=""
        self.tag +=   f"{self.add_spaces(indent)}<{ r'/' if self.tag_type==Tag.Close else ''}{self.markup}"
        if self.inline:
            self.tag += " style=\"" + self.inline + "\""
        if self.tag_type==Tag.Span:
            self.tag += f">{self.val}</{self.markup}>"
        else:
            self.tag += f">{self.val if self.val else ''}"

        if is_break:
            self.tag +="\n"
        return self.tag

class U_list(Element):



    def __init__(self,label,li,indent=0):
        super(Element,self)
        self.label=label
        self.li=li
        self.indent=indent


    def make_list(self):
        self.ul = Element(Tag.Open,markup="ul",val=self.label ).make_tag(indent=self.indent)

        for i,j in self.li.items():
            self.ul += (Element(Tag.Span,markup="li",val=j,inline=i).make_tag(indent=self.indent+2) )

        self.ul += Element(Tag.Close, markup="ul",val="").make_tag(indent=self.indent)

        return self.ul

