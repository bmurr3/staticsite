import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node  = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")

        self.assertNotEqual(node, node2)

        node  = TextNode("This is a text node", "bold", "https://www.youtube.com")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")

        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node  = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")

        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node  = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")

        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()
