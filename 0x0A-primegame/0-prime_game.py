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
        if nums[round_num] < 0:
            return None  # Invalid input, return None

        current_nums = list(range(1, nums[round_num] + 1))

        while any(is_prime(num) for num in current_nums):
            prime = min(num for num in current_nums if is_prime(num))
            current_nums = [n for n in current_nums if n % prime != 0]

        # If no prime numbers left, the player cannot make a move and wins
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

# Testing the revised function with additional test cases
# print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
# print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
# print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
# print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
# print("Winner: {}".format(isWinner(1, [1])))
# print("Winner: {}".format(isWinner(0, [0])))
# print("Winner: {}".format(isWinner(-1, [10])))
# nums = [0] * 100
# for i in range(100):
#    nums[i] = i * i
# print("Winner: {}".format(isWinner(100, nums)))
# nums = [0] * 10000
# for i in range(10000):
#    nums[i] = i
# print("Winner: {}".format(isWinner(10000, nums)))
