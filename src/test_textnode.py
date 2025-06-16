import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ne(self):
        tn = TextNode("This is code text", TextType.CODE)
        tn2 = TextNode("I am a link", TextType.LINK, "http://localhost")
        self.assertNotEqual(tn,tn2)
    
    def test_url_none(self):
        tn = TextNode("Italic", TextType.ITALIC)
        self.assertIsNone(tn.url)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()