#!/bin/bash/python3

def containsDuplicate(self, nums: List[int]) -> bool:
    """Funstion that checks if the list contains duplicates"""
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hash.add(n)
    return False