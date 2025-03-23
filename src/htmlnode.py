from typing import TypeAlias


TAG_TYPE: TypeAlias = str | None
VALUE_TYPE: TypeAlias = str | None
HTML_CHILD: TypeAlias = list["HTMLNode"] | None
PROPS_TYPE: TypeAlias = dict[str, str] | None


class HTMLNode():
    def __init__(
        self,
        tag: TAG_TYPE = None,
        value: VALUE_TYPE = None,
        children: HTML_CHILD = None,
        props: PROPS_TYPE = None
    ):
        self.tag: TAG_TYPE = tag
        self.value: VALUE_TYPE = value
        self.children: HTML_CHILD = children
        self.props: PROPS_TYPE = props

    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ''
        
        prop_repr = [f' {key}="{value}"' for key, value in self.props.items()]
        return ''.join(prop_repr)
    
    def __repr__(self) -> str:
        tag = self.tag
        value = self.value
        children = self.children
        props = self.props

        return f'{type(self).__name__}({tag=}, {value=}, {children=}, {props=}, {id(self)=})'
