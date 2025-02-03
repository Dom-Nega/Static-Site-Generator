from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
class TextType(Enum):
    # Add your enum members here for:
    TEXT = "text"       # Normal text
    BOLD = "bold"       # Bold text
    ITALIC = "italic"   # Italic text
    CODE = "code"       # Code text
    LINK = "link"       # Links
    IMAGE = "image"     # Images


class TextNode:
    
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and 
            self.text_type == other.text_type)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None,text_node.text)
            case TextType.BOLD:
                return LeafNode("b",text_node.text)
            case TextType.ITALIC:
                return LeafNode("i",text_node.text)
            case TextType.CODE:
                return LeafNode("code",text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href":text_node.url})
            case TextType.IMAGE:
                return LeafNode("img","",{"src":text_node.url, "alt":text_node.text})
            case _:
                raise ValueError("No Text Type or incorrect Text Type")
        