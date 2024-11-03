import textnode


def main():
    node = textnode.TextNode(
        "This is a Text Node",
        textnode.TextType.BOLD,
        "https://www.boot.dev"
    )

    print(node)


if __name__ == '__main__':
    main()
