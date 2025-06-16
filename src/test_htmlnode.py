import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_tag_is_none(self):
        tn = HTMLNode()
        self.assertIsNone(tn.tag)
    
    def test_prop_to_html(self):
        props_html = ' href="https://www.google.com" target="_blank"'
        tn = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(props_html,tn.props_to_html())
        
    def test_to_html(self):
        tn = HTMLNode("p","lorem ipsum")
        with self.assertRaises(NotImplementedError):
            tn.to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_nonetag(self):
        node2 = LeafNode(None, "Hello, world!")
        self.assertEqual(node2.to_html(), 'Hello, world!')
    
    def test_leaf_to_html_with_prop(self):
        node3 = LeafNode("p", "Hello, world!",{"color":"red"})
        self.assertEqual(node3.to_html(), '<p color="red">Hello, world!</p>')
    
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_no_children(self):
        pn = ParentNode("li",None,{"id":"somelist"})
        with self.assertRaises(ValueError):
            pn.to_html()
        

if __name__ == "__main__":
    unittest.main()