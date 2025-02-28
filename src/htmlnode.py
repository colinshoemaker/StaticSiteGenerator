class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == "" or self.props == {} or self.props == None:
            return ""
        
        attributes = " "
        for key, value in self.props.items():
            ea = f'{key}="{value}"'
            attributes = attributes + ea + " "
        return attributes[:-1]
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props ={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError 
        if self.tag == None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
