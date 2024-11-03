from typing import Self


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[Self] | None = None,
        props: dict[str, str] | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ''

        return ' '.join([
            f'{key}="{val}"' for key, val in self.props.items()
        ])

    def __repr__(self) -> str:
        return f"""
{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})
        """.strip()
