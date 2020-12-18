from typing import List
from collections import defaultdict
import os

file_name = 'words.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)


def get_words(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read().split()


def save_anagrams(file_path: str, data: List[List[str]]):
    with open(file_path, 'a', encoding='UTF-8') as file:
        for itm in data:
            file.write(', '.join(itm) + '\n')


def anagrams(words: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word in words:
        result[''.join(sorted(word))].append(word)
    return list(result.values())


# with open(file_path, 'r', encoding='UTF-8') as file:
#     file_data = file.read().split()
#     print(1)

file_words = get_words(file_path)
anagrams_list = anagrams(file_words)

result_file_path = os.path.join(os.path.dirname(__file__), 'anagrams_result.txt')
save_anagrams(result_file_path, anagrams(get_words(file_path)))
