import re

from textnode import TextType, TextNode


DELIMITERS: dict[TextType, str] = {
    TextType.BOLD: '**',
    TextType.CODE: '`',
    TextType.ITALIC: '*'
}
IMAGE_REGEX: str = r'!\[(.*?)\]\((.*?)\)'
LINK_REGEX: str = r'[^!]\[(.*?)\]\((.*?)\)'


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    delimiter = DELIMITERS[text_type]

    for node in old_nodes:
        node_text = node.text
        split_text = node_text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError('The text is not formatted correctly.')
        
        is_old: bool = True
        for segment in split_text:
            new_nodes.append(
                TextNode(
                    segment,
                    node.text_type if is_old else text_type
                )
            )
            is_old = not is_old

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    hits = re.findall(IMAGE_REGEX, text)
    return hits


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    hits = re.findall(LINK_REGEX, text)
    return hits


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        node_text: str = node.text

        images = extract_markdown_images(node_text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            delimiter = f'![{alt_text}]({url})'

            split_nodes = node_text.split(delimiter)

            first_part, *the_rest = split_nodes

            new_nodes.append(TextNode(
                first_part,
                text_type=node.text_type
            ))

            new_nodes.append(TextNode(
                alt_text,
                TextType.IMAGE,
                url
            ))

            node_text = ''.join(the_rest)

        new_nodes.append(TextNode(
            node_text,
            node.text_type
        ))

    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        node_text: str = node.text

        links = extract_markdown_links(node_text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for alt_text, url in links:
            delimiter = f'[{alt_text}]({url})'

            split_nodes = node_text.split(delimiter)

            first_part, *the_rest = split_nodes

            new_nodes.append(TextNode(
                first_part,
                text_type=node.text_type
            ))

            new_nodes.append(TextNode(
                alt_text,
                TextType.LINK,
                url
            ))

            node_text = ''.join(the_rest)

        new_nodes.append(TextNode(
            node_text,
            node.text_type
        ))

    return new_nodes
