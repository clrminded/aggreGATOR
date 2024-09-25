import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_init(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        test = node.__repr__()
        str = "TextNode(This is a text node, italic, https://www.boot.dev)"
        self.assertEqual(test, str)

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        same = node.__eq__(node2)
        self.assertEqual(same, True)

    def test_not_eq(self):
        node = TextNode("This should be the same", "bold", "https://www.boot.dev")
        test = TextNode("This is a test node", "bold")
        result = node.__eq__(test)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
