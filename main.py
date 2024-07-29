def open_file(path_to_file: str) -> str:
    """
    Read and store text based file

    Parameters:
        path_to_file (str): relative or absolute path to a file

    Returns:
        str: contents of read file
    """
    with open(path_to_file) as f:
        return(f.read())

def count_words(file: str) -> int:
    """
    Takes an opened file and returns the word count

    Parameters:
        file (str): contents of an opened file

    Returns:
        int: total word count
    """
    words = file.split()

    counter = 0
    for word in words:
        counter += 1
    
    return counter

def count_letters(file: str) -> dict:
    """
    Takes an opened file and returns a dictionary containing the count of each letter

    Parameters:
        file (str): contents of an opened file

    Returns:
        dict: total letter count
    """
    chars = {}

    for char in file:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def create_report(file: str):
    compiled_report = []
    
    for entry in count_letters(file):
        if entry.isalpha():
            compiled_report.append(entry)
    
    return compiled_report.sort(reverse=True)

if __name__ == '__main__':
    print(create_report(open_file("books/frankenstein.txt")))