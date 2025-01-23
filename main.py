from collections import defaultdict

def main():
    path_to_file = "books/frankstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
        char_count = defaultdict(lambda:0)
        words_count = len(file_contents.split())
        for c in file_contents:
            char_count[c.lower()] += 1

    sorted_char_count = [(count, char) for char, count in char_count.items()]
    sorted_char_count.sort(reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")

    for count, char in sorted_char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End Report ---")

main()

