import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTLMNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(
        tag="a",
        props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"' )
    
    def test_props_none(self):
        node = HTMLNode(props=None)
        result = node.props_to_html()
        self.assertEqual(result,"")

    def test_props_empty(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result,"")

    def test_prop_to_html(self):
        node = HTMLNode(
        tag="a",
        props={"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"' )
            
class TestLeafNode(unittest.TestCase):
     
    def test_to_HTML_no_prop(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        self.assertEqual(result, "<p>This is a paragraph of text.</p>")
    
    def test_to_HTML_props(self):
        node = LeafNode("p", "This is a paragraph of text.", {"href": "https://www.google.com", "target": "_blank"})
        result = node.to_html()
        self.assertEqual(result, '<p href="https://www.google.com" target="_blank">This is a paragraph of text.</p>')
    
    def test_to_HTML_empty_dict(self):
        node = LeafNode("p", "This is a paragraph of text.",{})
        result = node.to_html()
        self.assertEqual(result, "<p>This is a paragraph of text.</p>")

    def test_to_HTML_no_tag(self):
        node = LeafNode(None,"This is a paragraph of text.")
        result = node.to_html()
        self.assertEqual(result, "This is a paragraph of text.")

    def test_to_HTML_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

class TestParentNode(unittest.TestCase):
    def test_to_HTML_multiple_children(self):
        node = ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),],)
        result = node.to_html()
        self.assertEqual(result, '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_HTML_single_child(self):
        node = ParentNode("p",[
            LeafNode("b", "Bold text")],)
        result = node.to_html()
        self.assertEqual(result, '<p><b>Bold text</b></p>')
                         
    def test_to_HTML_mutli_parent(self):
        node = ParentNode("p",[ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),],)],)
        result = node.to_html()
        self.assertEqual(result, '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')

    def test_to_HTML_no_children(self):
        node = ParentNode("p",None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have a child")

    def test_to_HTML_no_tag(self):
        node = ParentNode(None, [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have a tag")


if __name__ == "__main__":
    unittest.main()