import unittest
from typing import Final

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_default_initializer(self):
        node = HTMLNode()

        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_tag(self):
        node = HTMLNode(tag="a")

        self.assertEqual(node.tag, "a")

    def test_value(self):
        node = HTMLNode(value="This is a test")

        self.assertEqual(node.value, "This is a test")

    def test_children(self):
        node1 = HTMLNode()
        node2 = HTMLNode()

        children_list = [node1, node2]

        node = HTMLNode(children=children_list)

        self.assertIs(node.children, children_list)

    def test_props(self):
        test_props = dict(
            prop1="Test Prop 1",
            prop2="Test Prop 2"
        )

        node = HTMLNode(props=test_props)

        self.assertIs(node.props, test_props)

    def test_to_html_not_implemented(self):
        node = HTMLNode()

        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        TEST_PROPS: Final[dict[str, str]] = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        EXPECTED_STR: Final[str] = (
            'href="https://www.google.com"'
            ' target="_blank"'
        )

        node = HTMLNode(props=TEST_PROPS)

        self.assertEqual(node.props_to_html(), EXPECTED_STR)


if __name__ == '__main__':
    unittest.main()
