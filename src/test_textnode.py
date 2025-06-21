import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimeter


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
    
    def test_split_bold(self):
        node = TextNode("This is a normal **with bold** and `code`", TextType.NORMAL) 
        new_nodes = split_nodes_delimeter([node],"**",TextType.BOLD)
        expected_nodes = [
            TextNode("This is a normal " , TextType.NORMAL),
            TextNode("with bold" , TextType.BOLD),
            TextNode(" and `code`", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes,expected_nodes)
    
    
    def test_split_code(self):
        node = TextNode("This is a normal and `code text`", TextType.NORMAL) 
        new_nodes = split_nodes_delimeter([node],"`",TextType.CODE)
        expected_nodes = [
            TextNode("This is a normal and " , TextType.NORMAL),
            TextNode("code text", TextType.CODE)
        ]
        self.assertEqual(new_nodes,expected_nodes)

    def test_split_italic(self):
        node = TextNode("_This is italic_", TextType.NORMAL) 
        new_nodes = split_nodes_delimeter([node],"_",TextType.ITALIC)
        expected_nodes = [TextNode("This is italic" , TextType.ITALIC)]
        self.assertEqual(new_nodes,expected_nodes)
    
    def test_split_not_closed_delimiter(self):
        node = TextNode("_This is italic", TextType.NORMAL) 
        with self.assertRaises(ValueError):
            split_nodes_delimeter([node],"_",TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()