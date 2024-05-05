from typing import Self


class TextNode:
    def __init__(
        self,
        text: str,
        text_type: str,
        url: str = None
    ):
        self.text      = text
        self.text_type = text_type
        self.url       = url

    def __eq__(
        self,
        to_compare: Self
    ):
        return (
            self.text == to_compare.text 
            and self.text_type == to_compare.text_type 
            and self.url == to_compare.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
