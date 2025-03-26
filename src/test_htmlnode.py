import unittest

from htmlnode import HTMLNode

test_list = [1, 2, 3]
test_dict = {"href": "https://www.google.com"}

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<b>", "Some text goes here")
        node2 = HTMLNode("<b>", "Some text goes here")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("<b>", "Some text goes here", test_list)
        node2 = HTMLNode("<b>", "Some text goes here", test_list, test_dict)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("<p>", "Some text goes here", test_list, test_dict)
        node2 = HTMLNode("<b>", "Some text goes here", test_list, test_dict)
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("<b>", "Some text goes here", test_list, test_dict)
        self.assertEqual(
            ' href="https://www.google.com"',
            node.props_to_html(),
        )


if __name__ == "__main__":
    unittest.main()