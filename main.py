def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(get_length(file_contents))

def get_length(string):
    words = string.split()
    number_of_words = len(words)
    return number_of_words

main()