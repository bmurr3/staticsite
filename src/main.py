from leafnode import LeafNode
from textnode import TextNode


VALID_TEXT_NODE_TYPES = [
    'text',
    'bold',
    'italic',
    'code',
    'link',
    'image'
]

def text_node_to_html_node(
    text_node: TextNode
) -> LeafNode:
    if not text_node.text_type in VALID_TEXT_NODE_TYPES:
        raise ValueError(f"TextNode of type '{text_node.text_type}' not convertable.")
    
    if text_node.text_type == 'text':
        return LeafNode(
            value=text_node.text
        )
    
    if text_node.text_type == 'bold':
        return LeafNode(
            tag='b',
            value=text_node.text
        )
    
    if text_node.text_type == 'italic':
        return LeafNode(
            tag='i',
            value=text_node.text
        )
    
    if text_node.text_type == 'code':
        return LeafNode(
            tag='code',
            value=text_node.text
        )
    
    if text_node.text_type == 'link':
        return LeafNode(
            tag='a',
            value=text_node.text,
            props={
                'href': text_node.url
            }
        )
    
    if text_node.text_type == 'image':
        return LeafNode(
            tag='img',
            props={
                'src': text_node.url,
                'alt': text_node.text
            }
        )
    
    return None


def split_nodes_delimiter():
    pass


def main():
    node = TextNode("This is a text node", "bold", "https//www.boot.dev")
    print(node)


if __name__ == '__main__':
    main()