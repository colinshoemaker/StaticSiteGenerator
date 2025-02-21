from textnode import TextNode
from textnode import TextType


def main():
    new = TextNode('here is some text', TextType.BOLD, 'fakeurl.com' )
    print(new)
    
if __name__ == "__main__":
    main()
