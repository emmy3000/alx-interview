#!/usr/bin/python3
"""
Script: 0-prime_game
"""


def is_prime(num):
    """
    Determine the winner of a series of prime game rounds.

    Args:
    - x (int): The number of rounds to be played.
    - nums (List[int]): An array of integers representing
    the ending values (n) for each round.

    Returns:
    - str or None: The name of the player who won the most rounds
    (either "Maria" or "Ben"). If the winner cannot be determined, 
    returns None.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_make_move(nums, primes):
        for p in primes:
            if p in nums:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        round_nums = list(range(1, nums[i] + 1))
        primes = get_primes(nums[i])

        maria_turn = True
        while can_make_move(round_nums, primes):
            selected_prime = min([p for p in primes \
                    if p in round_nums])
            round_nums = [num for num in round_nums \
                    if num % selected_prime != 0]

            if maria_turn:
                maria_turn = False
            else:
                maria_turn = True

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
