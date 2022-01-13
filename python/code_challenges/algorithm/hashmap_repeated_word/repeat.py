
from hashtable import HashTable
import re

def hashmap_repeated_word(text):
    ht = HashTable()
    count = 0
    t = re.findall(r'\w+', text)
    for word in t:
        word = word.lower()
        print(word)
        if ht.contains(word):
            return word
        else:
            ht.add(word, count)
            count += 1
    return None
