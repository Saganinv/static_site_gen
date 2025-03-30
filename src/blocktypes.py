from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered_list"
    ORLIST = "ordered_list"

def block_to_block_type(block):
    lines = [line.strip() for line in block.split("\n") if line.strip()]

    print(lines)
    for line in lines:
        print(line[0])
    
    if block.startswith("#"):
        return BlockType.HEAD
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNLIST
    elif all(line[0].isdigit() for line in lines):
        # Additional check for sequential numbers could be added here.
        # We'll see if this comes back to bite me.
        return BlockType.ORLIST
    else:
        return BlockType.PARA
