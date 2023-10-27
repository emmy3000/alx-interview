#!/usr/bin/python3
"""
UTF-8 Encoding Validator
"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    Args:
    data (List[int]): A list of integers where each integer
    represents 1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for char_d in data:
        byte = char_d & 0xff

        if num_bytes == 0:
            if byte < 0x80:
                # Single-byte character (0xxxxxxx)
                num_bytes = 0
            elif byte < 0xC0:
                # Invalid start byte (10xxxxxx)
                return False
            elif byte < 0xE0:
                # Two-byte character (110xxxxx)
                num_bytes = 1
            elif byte < 0xF0:
                # Three-byte character (1110xxxx)
                num_bytes = 2
            elif byte < 0xF8:
                # Four-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid start byte (11111xxx)
                return False
        else:
            if byte < 0x80 or byte >= 0xC0:
                # Invalid continuation byte (not 10xxxxxx)
                return False
            num_bytes -= 1

    return num_bytes == 0
