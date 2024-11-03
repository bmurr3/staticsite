import unittest
from typing import Final

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "localhost:8888")
        node2 = TextNode("This is a text node", TextType.BOLD, "localhost:8888")
        self.assertEqual(node, node2)

    def test_identity_without_url(self):
        EXPECTED_TEXT: Final[str] = "This is a text node."
        TEST_ENUM: Final[TextType] = TextType.ITALIC
        EXPECTED_ENUM_VAL: Final[str] = TEST_ENUM.value

        node = TextNode(EXPECTED_TEXT, TEST_ENUM)

        self.assertEqual(node.text, EXPECTED_TEXT)
        self.assertEqual(node.text_type, EXPECTED_ENUM_VAL)
        self.assertIsNone(node.url)

    def test_identity_with_url(self):
        EXPECTED_TEXT: Final[str] = "This is a text node."
        TEST_ENUM: Final[TextType] = TextType.IMAGE
        EXPECTED_ENUM_VAL: Final[str] = TEST_ENUM.value
        EXPECTED_URL: Final[str] = "localhost:8888"

        node = TextNode(EXPECTED_TEXT, TEST_ENUM, EXPECTED_URL)

        self.assertEqual(node.text, EXPECTED_TEXT)
        self.assertEqual(node.text_type, EXPECTED_ENUM_VAL)
        self.assertEqual(node.url, EXPECTED_URL)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
