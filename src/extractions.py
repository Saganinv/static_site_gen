from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
             raise ValueError(f"Invalid Markdown syntax: Unmatched delimiter '{delimiter}' in text '{node.text}'")

        for i, part in enumerate(parts):
            if not part:  # Skip empty strings resulting from adjacent delimiters or start/end delimiters
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        parts = re.split(r"!\[.*?\]\(.*?\)", node.text)
        for i, part in enumerate(parts):
            if not part:  # Skip empty strings resulting from adjacent delimiters or start/end delimiters
                continue
            
            new_nodes.append(TextNode(part, TextType.TEXT))
            
            if i < len(images):
                new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        parts = re.split(r"\[.*?\]\(.*?\)", node.text)
        for i, part in enumerate(parts):
            if not part:  # Skip empty strings resulting from adjacent delimiters or start/end delimiters
                continue
            
            new_nodes.append(TextNode(part, TextType.TEXT))
            
            if i < len(links):
                new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
    return new_nodes