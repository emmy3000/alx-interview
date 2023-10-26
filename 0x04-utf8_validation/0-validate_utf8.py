#!/usr/bin/env python3
"""
Script used for determining if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set represents
    a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers where each integer
        represents 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    bytes_to_follow = 0

    for num in data:
        binary_representation = format(num, '08b')

        if bytes_to_follow == 0:
            if binary_representation[0] == '0':
                bytes_to_follow = 0
            elif binary_representation[0] == '1':
                if binary_representation.count('1') >= 2:
                    bytes_to_follow = binary_representation.index('0')
                    if bytes_to_follow == 1 or bytes_to_follow > 4:
                        return False
                else:
                    return False
        else:
            if binary_representation[:2] == '10':
                bytes_to_follow -= 1
            else:
                return False

    return bytes_to_follow == 0
