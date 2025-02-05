def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = get_length(file_contents)
    num_characters_dict = count_characters(file_contents)
    print(num_characters_dict)

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

main()