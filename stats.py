from collections import defaultdict

def get_num_words(file_content: str) -> int:
    return len(file_content.split())

def get_char_count(file_content: str) -> dict:
    char_count = defaultdict(lambda:0)
    for c in file_content:
        char_count[c.lower()] += 1

    return char_count
