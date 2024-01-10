#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    Name = list(a_dictionary.keys())[0]
    score = a_dictionary[Name]
    for i, v in a_dictionary.items():
        if v >= score:
            score = v
            Name = i
    return Name
