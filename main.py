def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = get_length(file_contents)
    characters_dict = count_characters(file_contents)
    print_report(characters_dict, num_words)

def get_length(string):
    words = string.split()
    number_of_words = len(words)
    return number_of_words

def count_characters(string):
    lowered_string = string.lower()
    my_dict = {}
    for c in lowered_string:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    return my_dict

def print_report(my_dict, total_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    print()
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    for key in sorted_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {sorted_dict[key]} times")
    print("--- End report ---")
        

main()