# 0x0A. Prime Game

This Python program implements a game where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers. The game is played for multiple rounds, and the winner of each round is determined based on optimal play by both players.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Function Details](#function-details)
- [Author](#author)

## Installation

No special installation is required. Simply download the `0-prime_game.py` file and include it in your project.

## Usage

The main functionality is provided by the `isWinner` function, which takes the number of rounds `x` and an array of integers `nums` as input. The function returns the name of the player who won the most rounds or `None` if the winner cannot be determined.

```python
from 0-prime_game import isWinner

# Example usage
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
```

**Example:**

Consider the following example:

```python
from 0-prime_game import isWinner

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
```

*The output for this example is:*

```
Winner: Ben
```

## Function Details

**`isWinner(x, nums)`**

Determine the winner of a series of prime game rounds.

*Parameters:*

- `x` (int): The number of rounds to be played.
- `nums` (List[int]): An array of integers representing the ending values (n) for each round.

*Returns:*

- `str` or `None`: The name of the player who won the most rounds (either "Maria" or "Ben"). If the winner cannot be determined, returns `None`.

**`remove_multiples_of_prime(primes, prime)`**

Function modifies the input list by removing multiples of the specified prime number.

*Parameters:*

- `primes` (List[int]): The list of numbers to remove multiples from.
- `prime` (int): The prime number whose multiples need to be removed.

*Returns:*

- `None`

## Author

Emeka Emodi
