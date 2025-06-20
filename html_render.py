#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self._content = [content]
        else:
            self._content = []
        if kwargs:
            self.attributes = kwargs


    def append(self, new_content):
        self._content.append(new_content)

    def _open_tag(self):
        if hasattr(self, "attributes"):
            parts = [f"<{self.tag}"]
            for key, value in self.attributes.items():
                parts.append(f'{key}="{value}"')
            return " ".join(parts) + ">"
        return f"<{self.tag}>"

    def _close_tag(self):
        return f"</{self.tag}>"

    def render(self, out_file):
        out_file.write(self._open_tag() + "\n")
        for item in self._content:
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(item)
            out_file.write("\n")
        out_file.write(self._close_tag())


class Html (Element):
    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file)


class Body (Element):
    tag = "body"


class P (Element):
    tag = "p"


class Head (Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(f"{self._open_tag()}{self._content[0]}{self._close_tag()}")

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag (Element):
    def render(self, out_file):
        temp_tag = self._open_tag()
        temp_tag = temp_tag[:-1]
        temp_tag += " />\n"
        out_file.write(temp_tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A (OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class UL(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class Header (OneLineTag):
    def __init__(self, font, content=None, **kwargs):
        self.tag = "h"+ str(font)
        super().__init__(content, **kwargs)