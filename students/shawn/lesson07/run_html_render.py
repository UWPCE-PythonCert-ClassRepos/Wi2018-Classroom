import  os
from html_render import Element,Tag,Unord_list,Table




with open("mydoc.html",'w') as file:
    file.write(Element(Tag.Open,markup="html").make_tag())
    file.write(Element(Tag.Open,markup="body").make_tag())

    file.write(Element(Tag.Span, markup="h1",val="Python Class - Html rendering example").make_tag())
    file.write(Element(Tag.Open, markup="p").make_tag(indent=2,is_break=False))

    file.write(Element(Tag.Span, markup="i"
                       ,inline="text-align:center;"
                       ,val="Here is a paragraph of text -- "
                            "there could be more of them, but this is enough to show that "
                            "we can do some text").make_tag(is_break=False))

    file.write(Element(Tag.Close, markup="p").make_tag())

    file.write(Element(Tag.Span, markup="hr",val="").make_tag(indent=2))

    file.write(Unord_list("", {"color:red": "First item in the list"
                      ,"font-style:italic":"Second item in the list"
                      ,"0":"<a href=\"http:\\www.google.com\">Link</a> to Google"}, indent=2).make_list())

    file.write(Element(Tag.Span, markup="hr",val="").make_tag(indent=2))

    file.write(Table("NHL Players", [("0","Name") ,("0","Position"),("0","Team")],
                                    [("0",["Chara","Defenseman","Bruins"]) ,
                                    ("0",["Marchand","Left Wing","Bruins"])], indent=2).make_table())

    file.write(Element(Tag.Close,markup="body").make_tag())
    file.write(Element(Tag.Close,markup="html").make_tag())




