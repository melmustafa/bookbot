def main() -> None:
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        words = book_content.split()
        letter_count = LettersCount(book_content)
        print(f"=================================== {book.name} ===================================")
        print(f"{len(words)} words found in the document")
        print()
        letters = [{"letter": letter, "count": letter_count[letter]} for letter in letter_count]
        letters.sort(reverse = True, key = sort_on)
        for entry in letters:
            print(f"The letter '{entry["letter"]}' appeared {entry["count"]} times")
        book.close()

def LettersCount(text: str) -> dict:
    result = {}
    lower_text = text.lower()
    for char in lower_text:
        if not char.isalpha():
            continue
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result

def sort_on(dic: dict) -> int:
    return dic["count"]

if __name__ == "__main__":
    main()