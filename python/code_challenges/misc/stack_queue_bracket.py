from collections import Counter

def validate_brackets(string):
    base = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    counts = dict(Counter(string))
    counts = {**base, **counts}
    return counts['('] == counts[')'] and counts['['] == counts[']'] and counts['{'] == counts['}']
