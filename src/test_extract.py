import unittest

from extract import extract_markdown_links,extract_markdown_images

class TestExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and with a [link](https://google.com)")
        self.assertListEqual([("link", "https://google.com")], matches)