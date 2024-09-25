from textnode import TextNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node.__repr__())

if __name__ == "__main__":
    main()
