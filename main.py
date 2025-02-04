from pprint import pprint

def sort_on(dict):
    return dict["num"]

def main():
    with open('books/frankenstein.txt') as f:
        book = f.read().lower()
        char_dict = {}
        for character in book:
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1
        
        char_list = []

        for key, value in char_dict.items():
            if key.isalpha():
                char_list.append({"char": key, "num": value})

        char_list.sort(reverse=True, key=sort_on)
        
        for stuff in char_list:
            letter = stuff['char']
            number = stuff['num']

            print(f"The '{letter}' character was found {number} times")

main()
