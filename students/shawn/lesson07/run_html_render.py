import  os
from html_render import Element,Tag,U_list


with open("mydoc.html",'w') as file:
    file.write(Element(Tag.Open,markup="html").make_tag())
    file.write(Element(Tag.Open,markup="body").make_tag())

    file.write(Element(Tag.Span, markup="h1",val="Python Class - Html rendering example").make_tag())
    file.write(Element(Tag.Open, markup="p").make_tag())
    file.write(Element(Tag.Span, markup="i"
                       ,inline="text-align:center;"
                       ,val="Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text").make_tag())
    file.write(Element(Tag.Close, markup="p").make_tag())


    file.write(U_list(" ",["The first item in a list", "The second item in a list","And this is a link to google"]).make_list())

    file.write(Element(Tag.Close,markup="html").make_tag())
    file.write(Element(Tag.Close,markup="body").make_tag())


