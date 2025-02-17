from textnode import TextNode, TextType
from inlinenodes import text_to_textnodes

def main():
    node = TextNode("this is a test", TextType.BOLD, "www.hello.com")
    print(node)

if __name__ == "__main__":
    main()