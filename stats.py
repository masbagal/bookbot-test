
def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    result = {}
    for char in text:
        c = char.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def sort_count(dict):
    return dict["count"]

def print_stats(path, word_count, char_count):
    sorted_list = []
    for char in char_count:
        if char.isalpha():
            sorted_list.append({ "char": char, "count": char_count[char] })
    sorted_list.sort(key=sort_count, reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["count"]}")

