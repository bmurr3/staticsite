from typing import Self

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        props: dict[str, str] = None
    ) -> Self:
        super().__init__(
            self=self,
            tag=tag,
            value=value,
            props=props
        )
    
    def to_html(self) -> str:
        html = '' if self.value is None else self.value

        if self.tag is None:
            return html
        
        html = f'<{self.tag}{self.props_to_html()}/>' if html == '' \
                else f'<{self.tag}{self.props_to_html()}>{html}</{self.tag}>'
        
        return html
    
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props_to_html()})'
