#!/usr/bin/python3

def mergeAlternatively():
    """type word = str type word2 = str
    return type: str
    """
    i, j = 0, 0
    
    result = []
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    result.append(word1[i:])
    result.append(word1[j:])
    return "".join(result)