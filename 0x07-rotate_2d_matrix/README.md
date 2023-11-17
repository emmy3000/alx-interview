# 0x07. Rotate 2D Matrix

This project provides a Python implementation for rotating a given n x n 2D matrix 90 degrees clockwise in-place. The main script, `0-rotate_2d_matrix.py`, contains the implementation, while testing is carried out in the `main_0.py` module.

## Implementation Details

### Function Definition (`0-rotate_2d_matrix.py`):

The core functionality is implemented in the `rotate_2d_matrix` function. Key points about the implementation include:

*Function Signature*:

```python
def rotate_2d_matrix(matrix):
```

*Description*:

Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

*Parameters*:

`matrix` (list of lists): Input matrix to be rotated.

*Algorithm*:

The implementation follows a two-step process:
- Transpose the matrix (swap rows with columns).
- Reverse each row to obtain the final rotated matrix.

### Test Module (`main_0.py`):

Testing is performed in the `main_0.py` script. This module imports the `rotate_2d_matrix` function and applies it to a sample matrix. The expected output is then printed for verification.

The main module definiton:
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


Expected output:
```shell
$ ./main.py
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Important Considerations

**Adherence to Instructions:**

The implementation strictly adheres to the provided instructions:

- The function is named `rotate_2d_matrix`.
- It does not return anything but edits the matrix in-place.
- It assumes the matrix has 2 dimensions and will not be empty.

**Edge Cases:**

The implementation accounts for various edge cases:

- Matrices of different sizes (3x3, 4x4, 2x2, 1x1).
- In-place rotation is handled correctly for square matrices.

**Space-Time Complexity:**

- *Time Complexity*: **O(N^2)** - The nested loops iterate through each element in the matrix.
- *Space Complexity*: **O(1)** - The rotation is performed in-place without using additional space.

## Workflow Breakdown:

*Transpose Matrix*:
	- Iterate through each element, swapping elements across the main diagonal.

*Reverse Each Row*:
	- Iterate through each row, reversing the elements to achieve the final rotated matrix.

## Author

Emeka Emodi
