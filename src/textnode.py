from enum import Enum
from typing import Any


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str | None = None
    ) -> None:
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, to_compare: Any) -> bool:
        if not isinstance(to_compare, TextNode):
            raise ValueError(f"Is not an instance of {self.__class__.__name__}")
        
        return all([
            self.text == to_compare.text,
            self.text_type == to_compare.text_type,
            self.url == to_compare.url
        ])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
