from typing import Self

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] = None
    ) -> Self:
        if not tag or tag is None:
            raise ValueError("Invalid ParentNode. Tag is not provided.")
        
        if not children or children is None or len(children) == 0:
            raise ValueError("Invalid ParentNode. Children nodes are not provided.")
        
        super().__init__(
            self=self,
            tag=tag,
            children=children,
            props=props
        )
    
    def to_html(self) -> str:
        html = ''

        for child in self.children:
            html = f'{html}{child.to_html()}'
        
        html = f'<{self.tag}{self.props_to_html()}>{html}</{self.tag}>'

        return html
    
    def __repr__(self) -> str:
        return f'ParentNode({self.tag}, {self.value}, {len(self.children) if self.children is not None else None}, {self.props_to_html()})'
