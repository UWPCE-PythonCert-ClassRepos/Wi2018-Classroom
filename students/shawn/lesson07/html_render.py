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
        """
        Create an HTML tag as either an opening or closing tag or a complete tag and add inline styles and
        indentation for printing as text

        :param indent: (int) number of spaces to indent the element in the file
        :param is_break: (bool) indicates if there should be a newline at the end of the line
        :return: (str) HTML element
        """
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

class Unord_list(Element):


    def __init__(self,label,li,indent=0):
        super(Element,self)
        self.label=label
        self.li=li
        self.indent=indent


    def make_list(self):
        """
        Create an unordered list with optional inline styles

        :return: (str) HTML list element
        """
        self.ele = Element(Tag.Open, markup="ul", val=self.label).make_tag(indent=self.indent)

        for i,j in self.li.items():
            self.ele += (Element(Tag.Span, markup="li", val=j, inline=i).make_tag(indent=self.indent + 2))

        self.ele += Element(Tag.Close, markup="ul", val="").make_tag(indent=self.indent)

        return self.ele


class Table(Element):

    def __init__(self,caption,tbl_head,tbl_cells,indent=0):
        super(Element,self)
        self.caption=caption
        self.tbl_head=tbl_head
        self.tbl_cells=tbl_cells
        self.indent=indent

    def make_table(self):
        """
        Create an HTML table with optional inline styles
        :return:
        """

        self.ele = Element(Tag.Open,markup="table",
                           inline="border: 1px solid black;border-collapse: collapse;")\
                            .make_tag(indent=self.indent)

        self.ele += Element(Tag.Span, markup="caption",val=self.caption).make_tag(indent=self.indent+2)

        # Header row
        self.ele += Element(Tag.Open, markup="tr").make_tag(indent=self.indent + 2)
        for i in self.tbl_head:
            self.ele += (Element(Tag.Span, markup="th", val=i[1], inline=i[0]).make_tag(indent=self.indent+4))
        self.ele += Element(Tag.Close, markup="tr").make_tag(indent=self.indent + 2)

        # Write the table body
        for i in self.tbl_cells:
            self.ele += Element(Tag.Open, markup="tr").make_tag(indent=self.indent + 2)
            for j in i[1]:
                self.ele += (Element(Tag.Span, markup="td", val=j, inline=i[0]).make_tag(indent=self.indent+4))

            self.ele += Element(Tag.Open, markup="tr").make_tag(indent=self.indent + 2)
        self.ele += Element(Tag.Close, markup="table").make_tag(indent=self.indent)

        return  self.ele

