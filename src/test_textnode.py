import os
import unittest
import yaml

from textnode import TextNode, TextType


PARAM_FILE: str = os.path.join(
    os.curdir,
    'src',
    'test_params',
    'textnode.yaml'
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        params = None
        with open(PARAM_FILE) as f:
            params = yaml.safe_load(f)

        params: list[dict[str, str]] = params['test_eq']

        node = TextNode(
            params[0]['text'],
            TextType[params[0]['text_type']],
            params[0]['url']
        )
        node2 = TextNode(
            params[1]['text'],
            TextType[params[1]['text_type']],
            params[1]['url']
        )
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        params = None
        with open(PARAM_FILE) as f:
            params = yaml.safe_load(f)

        params: list[dict[str, str]] = params['test_eq_with_url']

        node = TextNode(
            params[0]['text'],
            TextType[params[0]['text_type']],
            params[0]['url']
        )
        node2 = TextNode(
            params[1]['text'],
            TextType[params[1]['text_type']],
            params[1]['url']
        )
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        params = None
        with open(PARAM_FILE) as f:
            params = yaml.safe_load(f)

        params: dict[str, list[str] | str | None] = params['test_not_eq_text']

        node = TextNode(
            params['text'][0],
            TextType[params['text_type']],
            params['url']
        )
        node2 = TextNode(
            params['text'][1],
            TextType[params['text_type']],
            params['url']
        )

        self.assertNotEqual(
            node,
            node2
        )

    def test_not_eq_type(self):
        params = None
        with open(PARAM_FILE) as f:
            params = yaml.safe_load(f)

        params: dict[str, list[str] | str | None] = params['test_not_eq_type']

        node = TextNode(
            params['text'],
            TextType[params['text_type'][0]],
            params['url']
        )
        node2 = TextNode(
            params['text'],
            TextType[params['text_type'][1]],
            params['url']
        )

        self.assertNotEqual(
            node,
            node2
        )


if __name__ == "__main__":
    unittest.main()
