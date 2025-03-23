from enum import StrEnum


class TextType(StrEnum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(
        self,
        text: str,
        text_type: TextType,
        url: str | None = None
    ) -> None:
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url

    def __eq__(self, value: "TextNode") -> bool:
        return (
            self.text == value.text and
            self.text_type == value.text_type and
            self.url == value.url
        )
    
    def __repr__(self) -> str:
        text = self.text
        text_type = self.text_type.value
        url = self.url
        return f'{type(self).__name__}({text=}, {text_type=}, {url=}, {id(self)=})'
