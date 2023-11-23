# 0x08. Making Change

This project provides a Python implementation for solving the "Making Change" problem, which involves determining the fewest number of coins needed to meet a given total amount.

## Implementation

The core functionality is implemented in the `0-making_change.py` module. The `makeChange` function within this module takes a list of coin denominations (`coins`) and a target total amount (`total`) as input and returns the fewest number of coins needed to make change for the specified total. If the total cannot be met by any combination of coins, the function returns -1.

## Usage

To test the implementation, the `0-main.py` module is provided. It imports the `makeChange` function from `0-making_change.py` and demonstrates its usage with two example scenarios:

1. Test case with coin denominations [1, 2, 25] and a target total of 37:
    ```python
    makeChange([1, 2, 25], 37)
    ```
    Output: 7

2. Test case with coin denominations [1256, 54, 48, 16, 102] and a target total of 1453:
    ```python
    makeChange([1256, 54, 48, 16, 102], 1453)
    ```
    Output: -1

## How to Run

Execute the `0-main.py` module to see the results of the provided test cases.

```bash
./0-main.py
```

The output should display the fewest number of coins needed for each test case.

## Author
Emeka Emodi
