import unittest
from typing import Final

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_value_exception(self):
        self.assertRaises(
            ValueError,
            LeafNode,
            None, None
        )

    def test_to_html_no_tag(self):
        EXPECTED_VAL: Final[str] = "Hello World"

        node = LeafNode(None, EXPECTED_VAL)

        self.assertEqual(
            EXPECTED_VAL, node.to_html()
        )

    def test_to_html_tag_no_props(self):
        VALUE: Final[str] = "Hello World"
        TAG: Final[str] = "p"
        EXPECTED_OUTPUT: Final[str] = "<p>Hello World</p>"

        node = LeafNode(TAG, VALUE)

        self.assertEqual(EXPECTED_OUTPUT, node.to_html())

    def test_to_html_tag_props(self):
        VALUE: Final[str] = "Hello World"
        TAG: Final[str] = "a"
        PROPS: Final[dict[str, str]] = {
            "href": "https://www.google.com"
        }
        EXPECTED_OUTPUT: Final[str] = (
            '<a href="https://www.google.com">Hello World</a>'
        )

        node = LeafNode(TAG, VALUE, props=PROPS)

        self.assertEqual(EXPECTED_OUTPUT, node.to_html())
