#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None):
        if content is not None:
            self._content = [content]
        else:
            self._content = []


    def append(self, new_content):
        self._content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        print(f"content is {self._content}")
        for item in self._content:
            #out_file.write(item)
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(item)
            #item.render(out_file)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))


class Html (Element):
    pass

class Body (Element):
    tag = "body"

class P (Element):
    tag = "p"
class Head (Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        for item in self._content:
            out_file.write("<{tag}> {text} </{tag}>".format(tag=self.tag, text=item))
        #print(out_file)
class Title(OneLineTag):
    tag = "Title"
