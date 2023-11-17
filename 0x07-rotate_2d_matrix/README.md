# 0x07. Rotate 2D Matrix

This project provides a Python implementation for rotating an n x n 2D matrix 90 degrees clockwise in-place. The core functionality resides in the `0-rotate_2d_matrix.py` script, while testing is demonstrated in `main_0.py`.

## Implementation Details

### Function Definition (`0-rotate_2d_matrix.py`):

**Function Signature:**

```python
def rotate_2d_matrix(matrix):
```

**Description:**

- Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

**Parameters:**

- `matrix` (list of lists): The input matrix to be rotated.

**Algorithm:**

The implementation follows a two-step process:

1. **Transpose the Matrix (Swap Rows with Columns):**
- Iterate through each element, swapping elements across the main diagonal.

2. **Reverse Each Row:**
- Iterate through each row, reversing the elements to obtain the final rotated matrix.

### Test Module (`main_0.py`):

Testing is performed in the `main_0.py` script, which imports the `rotate_2d_matrix` function and applies it to a sample matrix. The expected output is then printed for verification.

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Expected Output:

```shell
$ ./main.py
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Important Considerations

### Adherence to Instructions:

- The function is named `rotate_2d_matrix`.
- It performs an in-place rotation without returning anything.
- *Assumption*: The matrix has 2 dimensions and is not empty.

### Handling Edge Cases:

The implementation accounts for various edge cases:

- Matrices of different sizes (3x3, 4x4, 2x2, 1x1).
- Ensures correct in-place rotation for square matrices.

### Space-Time Complexity:

- *Time Complexity*: **O(N^2)** - Due to the nested loops iterating through each matrix element.
- *Space Complexity*: **O(1)** - The rotation is performed in-place without using additional space.

## Workflow Breakdown:

*Transpose Matrix*:

- Iterate through each element, swapping elements across the main diagonal.

*Reverse Each Row*:

- Iterate through each row, reversing the elements to achieve the final rotated matrix.

## Conclusion

In this project, we successfully implemented a Python function, `rotate_2d_matrix`, to rotate an n x n 2D matrix 90 degrees clockwise in-place. The algorithm follows a two-step process: transposing the matrix by swapping rows with columns and then reversing each row. The script has been tested for various cases, including matrices of different sizes, and demonstrates adherence to given instructions.

The algorithm's time complexity is O(N^2), where N is the size of the matrix, and it achieves this rotation in-place with a space complexity of O(1). The workflow breakdown provides a clear overview of the steps involved.

Overall, the implementation addresses edge cases, strictly follows instructions, and provides an efficient solution for matrix rotation.

## Author

Emeka Emodi
