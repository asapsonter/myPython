import sys
import os

def searchForVowels(phrase:str) -> set:
    """return vowels found in supplied phrase"""

    vowels = set ( 'aeiou')

    return vowels.intersection(set(phrase))
def searchForletters(phrase:str, letters:str='aeiou') -> set:
    """returns set of letters"""
    return set(letters).intersection(set(phrase))
