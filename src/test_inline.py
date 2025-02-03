import unittest

from inlinenodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInline(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_node,[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ])
    
    def test_empty_text(self):
        node = TextNode("",TextType.TEXT)
        new_node = split_nodes_delimiter([node],"`", TextType.CODE)
        self.assertEqual(new_node,[TextNode("",TextType.TEXT)])

    def test_empty_delimiter(self):
        node = TextNode("This is a test with no delimiter",TextType.TEXT)
        with self.assertRaises(Exception) as context:
            new_node = split_nodes_delimiter([node],"",TextType.CODE)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")