from textnode import TextNode, TextType

def main():
    node = TextNode("this is a test", TextType.BOLD, "www.hello.com")
    print(node)


if __name__ == "__main__":
    main()