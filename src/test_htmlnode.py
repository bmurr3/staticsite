from htmlnode import HTMLNode

import unittest


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://google.com",
                "target": "_blank"
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )


if __name__ == '__main__':
    unittest.main()
