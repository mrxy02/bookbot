def get_book_text(path):
    with open(path) as text:
        text.contents = text.read()
    return text.contents

def main():
    file_path = "/Users/marcelrunzer/workspace/boot.dev/bookbot/books/frankenstein.txt"
    texts = get_book_text(file_path)
    print(texts)

main()
