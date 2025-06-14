import unittest

from htmlnode import HTMLNode,LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_tag_is_none(self):
        tn = HTMLNode()
        self.assertIsNone(tn.tag)
    
    def test_prop_to_html(self):
        props_html = 'href="https://www.google.com" target="_blank"'
        tn = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(props_html,tn.props_to_html())
        
    def test_to_html(self):
        tn = HTMLNode("p","lorem ipsum")
        with self.assertRaises(NotImplementedError):
            tn.to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Hello, world!")
        node3 = LeafNode("p", "Hello, world!",{"color":"red"})
        
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), 'Hello, world!')
        self.assertEqual(node3.to_html(), '<p color="red">Hello, world!</p>')

if __name__ == "__main__":
    unittest.main()