import generate_books
import json

O_FILE = 'result.txt'

def main():
    with open(O_FILE, 'w') as j_dump:
        json.dump(generate_books.dit_creator(count=100), j_dump, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()