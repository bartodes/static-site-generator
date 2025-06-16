from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode

def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None,text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i",text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text)
    
    if text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text,{"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img","",{"src": text_node.url,"alt": text_node.text})
    
    raise Exception("non existing TextNode type")

def main():
    tn = TextNode("test",TextType.NORMAL)
    print(tn)
    hn = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
    print(hn)
    ln = LeafNode("p", "Hello, world!",{"color":"red"})
    print(ln)

if __name__ == "__main__":
    main()