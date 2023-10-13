# 0x02. Minimum Operations

This task involves calculating the fewest number of operations needed to achieve a specified number of characters in a text file using **'Copy All'** and **'Paste'** operations. The character in question is 'H', and the task is to reach a specific number of 'H' characters in the file.

## Solution Implemented

The solution to this task is provided in a Python module named `0-minoperations.py`. It defines a function called `minOperations(n)` that takes an integer 'n' as its argument. This function calculates the fewest operations required to achieve the target number of 'H' characters using **'Copy All'** and **'Paste'** operations. If it's impossible to achieve the target, the function returns 0.

### Example

For example, given n = 9, the expected operations to reach the desired 'H' characters are as follows:

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHH => Paste => HHHHHHHHH

In this case, the number of operations is 6.

### Usage

The solution can be tested with a main module named `0-main.py`. This main module imports the `minOperations` function and provides test cases to demonstrate its functionality. For example, it calculates and prints the fewest operations to reach 4 and 12 'H' characters.

### Expected Output

Upon running the main module with the provided test cases, the expected output is as follows:

```bash
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7

```

The `minOperations` function should correctly determine the minimum number of operations needed to achieve the specified number of 'H' characters and return the result.
