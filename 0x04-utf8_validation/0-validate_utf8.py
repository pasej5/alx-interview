#!/usr/bin/env python3
"""
 method that determines if a given data set
 represents a valid UTF-8 encoding
"""


def validUTF8(data):
    '''
    Helper function to check if a byte is
    a valid start byte
    '''
    def is_start_byte(byte):
        '''
        Helper function to check if a byte
        is a valid continuation byte
        '''
        return (byte & 0b10000000) == 0b00000000

    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000
    i = 0
    while i < len(data):
        if (data[i] & 0b10000000) == 0b00000000:
            size = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            size = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            size = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            size = 4
        else:
            return False
        if i + size > len(data):
            return False
        for j in range(i + 1, i + size):
            if not is_continuation_byte(data[j]):
                return False
        i += size

    return True
