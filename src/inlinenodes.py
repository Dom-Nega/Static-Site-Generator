from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown syntax")
        split_string = node.text.split(delimiter)
        temp_node = []
        for i in range(len(split_string)):
            if i % 2 == 0:
                temp_node.append(TextNode(split_string[i], TextType.TEXT))
            if i % 2 != 0:
                temp_node.append(TextNode(split_string[i], text_type))
        new_nodes.extend(temp_node)
    return new_nodes

def extract_markdown_images(text):
    split_string = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    string = []
    for i in range(len(split_string)):
        if i % 2 != 0:
            
