from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode

def main():
    tn = TextNode("test",TextType.NORMAL)
    print(tn)
    hn = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
    print(hn)
    ln = LeafNode("p", "Hello, world!",{"color":"red"})
    print(ln)

if __name__ == "__main__":
    main()