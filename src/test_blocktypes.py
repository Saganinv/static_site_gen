import unittest
from blocktypes import BlockType, block_to_block_type

class TestMarkdownToHTML(unittest.TestCase):
    def test_header(self):
        md = "## This is **bolded** paragraph"
        
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.HEAD)

    def test_code(self):
        md = "``` code goes here ```"

        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.CODE)

    def test_ordered_line(self):
        md = """
        1. Pick up the phone
        2. I know he's only calling
        3. Cause he's drunk and alone
        """
        
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.ORLIST)


if __name__ == "__main__":
    unittest.main()
