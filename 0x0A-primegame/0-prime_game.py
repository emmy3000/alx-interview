#!/usr/bin/python3
"""
Script: 0-prime_game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game for multiple rounds.

    Args:
    - x (int): The number of rounds to be played.
    - nums (List[int]): A list of integers representing
      the upper limits for each round.

    Returns:
    - str or None: The name of the player who won the most rounds
    (either "Maria", "Ben") or None if it's a tie.
    """
    def is_prime(num):
        """
        Check if a given number is prime.

        Args:
        - num (int): The number to be checked.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for round_num in range(x):
        current_nums = list(range(1, nums[round_num] + 1))

        while any(is_prime(num) for num in current_nums):
            prime = min(num for num in current_nums if is_prime(num))
            current_nums = [n for n in current_nums if n % prime != 0]

        # If no prime nums left, the player can't make a move and win
        if not any(is_prime(num) for num in current_nums):
            if round_num % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
