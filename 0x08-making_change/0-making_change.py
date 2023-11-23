#!/usr/bin/python3
"""
@module: 0-making_change
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed
    to make change for a given total amount.

    Args:
       coins (list of int): Available coin denominations.
       total (int): Target total amount to make change for.

    Returns:
       int: Fewest number of coins needed for the total amount.
       Returns -1 if not possible.

    Notes:
       Assumes coin values are integers greater than 0.
       Assumes an infinite supply of each coin denomination.
    """
    # Check if the total is 0 or less
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number
    # of coins needed for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp array for each possible amount
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinite,
    # it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    # Return the min number of coins needed for the total amount
    return dp[total]
