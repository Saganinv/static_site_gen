from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # Only split nodes of type TEXT
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # If delimiter not in text, add node as is and continue
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        
        # Validate delimiter pairing - must have an odd number of parts
        # (meaning an even number of delimiters)
        if len(parts) % 2 == 0:
             raise ValueError(f"Invalid Markdown syntax: Unmatched delimiter '{delimiter}' in text '{node.text}'")

        # Process parts and add to new_nodes in order
        for i, part in enumerate(parts):
            if not part:  # Skip empty strings resulting from adjacent delimiters or start/end delimiters
                continue
            
            if i % 2 == 0:
                # Even index: plain text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index: text that was inside delimiters
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

node = TextNode("`code block` This is text with a word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)

# Example usage (can be removed or kept for testing)
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# node2 = TextNode("This is *italic* and **bold** text.", TextType.TEXT)
# node3 = TextNode("Plain text node.", TextType.TEXT)
# node4 = TextNode("`orphan delimiter", TextType.TEXT) # Should raise error
# old_nodes_list = [node, node2, node3]
# print("Original nodes:", old_nodes_list)
# split_code = split_nodes_delimiter(old_nodes_list, "`", TextType.CODE)
# print("After code split:", split_code)
# split_italic = split_nodes_delimiter(split_code, "*", TextType.ITALIC)
# print("After italic split:", split_italic)
# split_bold = split_nodes_delimiter(split_italic, "**", TextType.BOLD)
# print("After bold split:", split_bold)
# try:
#     split_nodes_delimiter([node4], "`", TextType.CODE)
# except ValueError as e:
#     print("Caught expected error:", e)
