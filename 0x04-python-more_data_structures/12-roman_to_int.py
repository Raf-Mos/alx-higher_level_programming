#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or len(roman_string) == 0 or
        not isinstance(roman_string, str):
        return 0
    som = 0
    saved_roman = 'I'
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'c': 100, 'D': 500, 'M': 1000}
    for n in reversed(range(len(roman_string))):
        if roman[romain_string[n]] >= roman[saved_roman]:
            saved_roman = roman_string[n]
            som += roman[roman_string[n]]
        else:
            som -= roman[roman_string[n]]
    return som
