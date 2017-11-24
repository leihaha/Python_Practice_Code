def word_count(phrase):
    p_list = phrase.split()
    print(p_list)
    p_set = set(p_list)
    print(p_set)
    for item in p_set:
        print("%s: %s" %(item, p_list.count(item)))


"""
import re

def word_count(phrase):
    words = re.findall(r"a-zA-Z0-9+(?:'\w)?", phrase.lower())
    return {word: words.count(word) for word in set(words)}
"""