
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        string = ""
        if not self.props:
            return string
        for prop, value in self.props.items():
            string += f' {prop}="{value}"'
        return string
    
    def __repr__(self):
        return "tag: {self.tag}\n value: {self.value}\n children: {self.children}\n prop: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if props is None:
            props = {}
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return html

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have a child")
        string = f'<{self.tag}>'
        for child in self.children:
            string += f'{child.to_html()}'
        string += f'</{self.tag}>'
        return string
    
