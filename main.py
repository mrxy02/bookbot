from stats import counter, letter_counter, splitter

def get_book_text(path):
    with open(path) as file:
        file.contents = file.read()
    return file.contents

def main():
    file_path = "/Users/marcelrunzer/workspace/boot.dev/bookbot/books/frankenstein.txt"
    texts = get_book_text(file_path)
    count_words = counter(texts)
    all_letters = letter_counter(texts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    letters_sorted = splitter(all_letters)
    for letter in letters_sorted:
        print(letter)
main()
