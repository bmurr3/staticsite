from typing import TypeAlias

from htmlnode import HTMLNode


TAG_TYPE: TypeAlias = str
CHILDREN_TYPE: TypeAlias = list[HTMLNode]
PROP_TYPE: TypeAlias = dict[str, str] | None


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: TAG_TYPE,
        children: CHILDREN_TYPE,
        props: PROP_TYPE = None
    ) -> None:
        super().__init__(
            tag=tag,
            children=children,
            props=props
        )

    def to_html(self):
        if self.tag is None:
            raise ValueError('A tag is required.')
        if self.children is None:
            raise ValueError('Children are required.')
        
        return (
            f'<{self.tag}{self.props_to_html()}>'
            f"{''.join([node.to_html() for node in self.children])}"
            f'</{self.tag}>'
        )
