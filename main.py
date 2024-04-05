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

