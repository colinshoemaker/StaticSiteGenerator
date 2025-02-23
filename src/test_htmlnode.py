import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_edict(self):
        node = HTMLNode(props={})
        assert node.props_to_html() == ""

    def test_estr(self):
        node = HTMLNode(props="")
        assert node.props_to_html() == ""

    def test_none(self):
        node = HTMLNode()
        assert node.props_to_html() == ""

    def test_str(self):
        node = HTMLNode(props={"key1": "value1", "key2": "value2"})
        assert node.props_to_html() == ' key1="value1" key2="value2"'
    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        assert node.props_to_html() == ' href="https://google.com"'


if __name__ == "__main__":
    unittest.main()