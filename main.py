def open_file(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return(f.read())

def count_words(file: str) -> int:
    words = file.split()

    counter = 0
    for word in words:
        counter += 1
    
    return counter

if __name__ == '__main__':
    print(count_words(open_file("books/frankenstein.txt")))