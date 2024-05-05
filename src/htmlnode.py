from typing import Self, NoReturn


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[Self] = None,
        props: dict[str, str] = None
    ) -> Self:
        self.tag      = tag
        self.value    = value
        self.children = children
        self.props    = props

    def to_html(self) -> NoReturn:
        raise NotImplementedError("'to_html' is not implemented.")

    def props_to_html(self) -> str:
        if self.props is None:
            return ''
        
        properties = ''
        for key, value in self.props.items():
            properties = f'{properties} {key}="{value}"'
        
        return properties

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {len(self.children) if self.children is not None else None}, {self.props_to_html()})'
