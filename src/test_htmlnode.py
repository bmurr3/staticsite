import unittest
import os
import yaml
from typing import Any

from htmlnode import HTMLNode


PARAM_FILE: str = os.path.join(
    os.curdir,
    'src',
    'test_params',
    'htmlnode.yaml'
)


class TestHTMLNode(unittest.TestCase):
    def get_params(self, test_name: str) -> dict[str, Any]:
        if not hasattr(self, 'params'):
            with open(PARAM_FILE) as f:
                self.params = yaml.safe_load(f)

        return self.params[test_name]
    
    def test_props_to_html_no_props(self):
        params = self.get_params('test_props_to_html_no_props')

        node = HTMLNode(
            props=params['props']
        )

        self.assertEqual(node.props_to_html(), params['expected_result'])

    def test_props_to_html_one_prop(self):
        params = self.get_params('test_props_to_html_one_prop')

        node = HTMLNode(
            props=params['props']
        )

        self.assertEqual(node.props_to_html(), params['expected_result'])

    def test_props_to_html_two_props(self):
        params = self.get_params('test_props_to_html_two_props')

        node = HTMLNode(
            props=params['props']
        )

        self.assertEqual(node.props_to_html(), params['expected_result'])


if __name__ == '__main__':
    unittest.main()