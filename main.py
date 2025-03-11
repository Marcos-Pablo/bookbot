from stats import get_num_words, get_char_count
import sys

def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    file_content = get_book_text(path_to_file)
    num_words = get_num_words(file_content)
    char_count = get_char_count(file_content)

    sorted_char_count = [(count, char) for char, count in char_count.items()]
    sorted_char_count.sort(reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count, char in sorted_char_count:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

main()

