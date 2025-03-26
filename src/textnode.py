from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "NORMAL_TEXT"
    BOLD_TEXT = "BOLD_TEXT"
    ITALIC_TEXT = "ITALIC_TEXT"
    CODE_TEXT = "CODE_TEXT"
    LINK_TEXT = "LINK_TEXT"
    IMAGE_TEXT = "IMAGE_TEXT"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    