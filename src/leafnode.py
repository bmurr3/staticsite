from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None
    ) -> None:
        if value is None:
            raise ValueError("A value is required.")
        
        super().__init__(
            tag=tag,
            value=value,
            props=props
        )

    def to_html(self) -> str:
        if self.tag is None:
            return self.value

        props_as_html = self.props_to_html()

        open_tag = (
            f'<{self.tag} {props_as_html}>'
            if props_as_html != ''
            else f'<{self.tag}>'
        )
        close_tag = f'</{self.tag}>'

        return f'{open_tag}{self.value}{close_tag}'
