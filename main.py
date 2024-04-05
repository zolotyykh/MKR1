import re
from collections import Counter

def read_text(filename: str) -> str:
    """
    Reads the content of the file with the specified name and returns it as a string.

    Parameters:
        filename (str): The name of the input file.

    Returns:
        str: The text from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def find_words(text: str) -> list:
    """
    Finds all the words in the text and returns them as a list.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of words.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def count_w_o(words: list) -> Counter:
    """
    Counts the occurrences of each word in the list and returns a dictionary with these counts.

    Parameters:
        words (list): The list of words.

    Returns:
        Counter: A Counter object with the counts of each word.
    """
    word_counts = Counter(words)
    return word_counts

def write_to_file(word_counts: Counter, output_filename: str) -> None:
    """
    Writes the most common words and their counts to a file.

    Parameters:
        word_counts (Counter): A Counter object with the counts of each word.
        output_filename (str): The name of the output file.

    Returns:
        None
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        for word, count in word_counts.most_common(10):
            file.write(f"{word}-{count}\n")

def main(input_filename: str, output_filename: str) -> None:
    """
    The main function of the program.

    Parameters:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.

    Returns:
        None
    """
    text = read_text(input_filename)
    words = find_words(text)
    word_counts = count_w_o(words)
    write_to_file(word_counts, output_filename)

if __name__ == "__main__":
    input_filename = "zolotyykh.txt"  # Specify the path to the input text file
    output_filename = "nastenka.txt"  # Specify the path to the output text file
    main(input_filename, output_filename)

