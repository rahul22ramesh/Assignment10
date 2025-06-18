#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None):
        self._content = [content]


    def append(self, new_content):
        self._content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for item in self._content:
            out_file.write(item)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))
