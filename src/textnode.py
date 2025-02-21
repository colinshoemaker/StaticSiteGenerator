from enum import Enum

class TextType(Enum):
    NORMAL = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(t1, t2):
        if t1.text == t2.text and t1.text_type == t2.text_type and t1.url == t2.url:
            return True
        else:
            return False
    def __repr__(textnode):
        return f"TextNode({textnode.text}, {textnode.text_type.value}, {textnode.url})"