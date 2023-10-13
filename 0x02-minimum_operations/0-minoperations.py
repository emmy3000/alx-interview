#!/usr/bin/env python3
"""
Calculates fewest operations to reach 'n' H characters.
"""


def minOperations(n):
    """
    Calculate the fewest operations to reach 'n' H characters
    using 'Copy All' and 'Paste'.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest operations needed to reach 'n' H characters,
        or 0 if impossible.
    """
    if n <= 1:
        return n  # Return n if n is 0 or 1

    pasted_chars, clipboard, counter = 1, 0, 0

    while pasted_chars < n:
        # If clipboard is empty, perform 'Copy All'
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        # If only one character is in the file, perform 'Paste'
        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars

        # If the clipboard contains more than needed, it's impossible
        if remaining < clipboard:
            return 0

        # If it's not possible to divide remaining characters evenly,
        # perform 'Paste'
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            # Perform 'Copy All' and 'Paste' as they're both needed
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    return counter if pasted_chars == n else 0
