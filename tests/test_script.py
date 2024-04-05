import pytest
import os
from main import read_text, find_words, count_w_o, write_to_file

@pytest.fixture
def sample_text():
    return "my name is nastia, my surname is zolotykh."

@pytest.fixture
def sample_words():
    return ["my", "name", "is", "nastia", "my", "surname", "is", "zolotykh"]

@pytest.fixture
def sample_word_counts():
    return {"my":2, "name":1, "is":2, "nastia":1, "my":2, "surname":1, "is":2, "zolotykh":1}

@pytest.fixture
def temp_text_file(sample_text):
    filename = "temp_text.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(sample_text)
    yield filename
    os.remove(filename)

def test_read_text(temp_text_file, sample_text):
    assert read_text(temp_text_file) == sample_text

def test_find_words(sample_text, sample_words):
    assert find_words(sample_text) == sample_words

@pytest.mark.parametrize("words, expected_counts", [
    (["zolotykh", "nastia", "zolotykh", "zolotykh", "nastia"], {"zolotykh": 3, "nastia": 2}),
    (["nastia", "nastia", "nastia", "nastia"], {"nastia": 4}),
    ([], {})
])
def test_count_word_occurrences(words, expected_counts):
    assert dict(count_w_o(words)) == expected_counts




