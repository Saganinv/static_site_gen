import unittest
from extractions import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_images, 
    split_nodes_links
)
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    #Test markdown image extraction
    def test_extract_markdown_images(self):
        text = "This is an image ![alt text](url/of/image.jpg) in markdown"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "url/of/image.jpg")])

    def test_extract_markdown_images_no_match(self):
        text = "This is a text without an image"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_multiple(self):
        text = "This is an image ![alt text](url/of/image.jpg) and another ![another alt](url/of/another.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "url/of/image.jpg"), ("another alt", "url/of/another.jpg")])

    def test_extract_markdown_images_no_alt_text(self):
        text = "This is an image ![](url/of/image.jpg) in markdown"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("", "url/of/image.jpg")])

    #Test markdown link extraction
    def test_extract_markdown_links(self):
        text = "This is a link [link text](url/of/link) in markdown"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "url/of/link")])

    def test_extract_markdown_links_no_match(self):
        text = "This is a text without a link"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_extract_markdown_links_multiple(self):
        text = "This is a link [link text](url/of/link) and another [another link](url/of/another)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "url/of/link"), ("another link", "url/of/another")])

    #Test split_nodes_images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    #Test split_nodes_links
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://www.google.com) and another [link](https://www.bing.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link", TextType.LINK, "https://www.bing.com"
                ),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()