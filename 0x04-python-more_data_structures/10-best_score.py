#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = sorted(a_dictionary.values(), reverse=True)[0]
    for k, v in a_dictionary.items():
        if v == best:
            return k
