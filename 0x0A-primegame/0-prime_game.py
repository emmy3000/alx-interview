#!/usr/bin/python3
"""
Script: 0-prime_game

Determine the most frequent winner in a series
of prime game rounds.
"""


def isWinner(x, nums):
    """
    Function determines the winner of the prime game
    for multiple rounds.

    Args:
    - x (int): The number of rounds to be played.
    - nums (List[int]): A list of integers representing
      the upper limits for each round.

    Returns:
    - str or None: The name of the player who won the most
      rounds (either "Maria", "Ben") or None if it's a tie.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    primes = [1 for _ in range(sorted(nums)[-1] + 1)]
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        remove_multiples_of_prime(primes, i)

    for i in nums:
        if sum(primes[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def remove_multiples_of_prime(primes, prime):
    """
    Helper function modifies the input list by removing
    multiples of the specified prime number.

    Args:
    - primes (List[int]): The list of numbers
      to remove multiples from.
    - prime (int): The prime number whose multiples
      need to be removed.

    Returns:
    - None
    """
    for i in range(2, len(primes)):
        try:
            primes[i * prime] = 0
        except (ValueError, IndexError):
            break
