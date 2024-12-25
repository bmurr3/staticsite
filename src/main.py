from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(
            value=text_node.text,
            tag=None
        )
    if text_node.text_type == TextType.BOLD:
        return LeafNode(
            value=text_node.text,
            tag='b'
        )
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(
            value=text_node.text,
            tag='i'
        )
    if text_node.text_type == TextType.CODE:
        return LeafNode(
            value=text_node.text,
            tag='code'
        )
    if text_node.text_type == TextType.LINK:
        return LeafNode(
            value=text_node.text,
            tag='a',
            props={
                'href': text_node.url
            }
        )
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            value='',
            tag='img',
            props={
                'src': text_node.url,
                'alt': text_node.text
            }
        )
    
    raise ValueError(f'Unknown Text Type: {text_node.text_type}')


def main() -> None:
    print(text_node_to_html_node(TextNode(
        'Test Node',
        TextType.BOLD
    )))


if __name__ == '__main__':
    main()
