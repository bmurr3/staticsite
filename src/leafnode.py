from typing import TypeAlias

from htmlnode import HTMLNode


VALUE_TYPE: TypeAlias = str
TAG_TYPE: TypeAlias = str | None
PROP_TYPE: TypeAlias = dict[str, str] | None


class LeafNode(HTMLNode):
    def __init__(
        self,
        value: VALUE_TYPE,
        tag: TAG_TYPE,
        props: PROP_TYPE = None
    ) -> None:
        super().__init__(
            tag=tag,
            value=value,
            props=props
        )

    def to_html(self) -> None:
        if self.value is None:
            raise ValueError('A value is required.')
        if self.tag is None:
            return self.value
        
        return (
            f'<{self.tag}{self.props_to_html()}>'
            f'{self.value}'
            f'</{self.tag}>'
        )
