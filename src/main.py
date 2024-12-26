import splitter
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


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes =[TextNode(
        text,
        TextType.NORMAL
    )]

    nodes = splitter.split_nodes_delimiter(nodes, TextType.CODE)
    nodes = splitter.split_nodes_delimiter(nodes, TextType.BOLD)
    nodes = splitter.split_nodes_delimiter(nodes, TextType.ITALIC)
    nodes = splitter.split_nodes_images(nodes)
    nodes = splitter.split_nodes_links(nodes)

    return nodes


def main() -> None:
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))


if __name__ == '__main__':
    main()
