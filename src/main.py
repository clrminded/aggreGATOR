from textnode import TextNode
from htmlnode import HTMLNode


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__repr__())

    props = {
        "href": "https://www.google.com", 
        "target": "_blank",
    }

    html_node = HTMLNode(None, None, None, props)
    print(html_node.props_to_html())

if __name__ == "__main__":
    main()
