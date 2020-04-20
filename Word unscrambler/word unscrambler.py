import json
from pathlib import Path

word = list(input('Word: '))                                       # Takes input
path = Path.home()/'Downloads/words_dictionary.json'               # Get words_dictionary.json from Downloads directory

with open(path, 'r') as file:                          
    data = json.loads(file.read())                                 # Load json data

word_set = sorted(word)                                            # Makes a set out of 'word'

for key in data.keys():
    key_set = sorted(key)                                          # Makes a set out of each key
    if key_set == word_set:
        print(key)
