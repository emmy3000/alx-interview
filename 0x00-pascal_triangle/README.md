# Pascal's Triangle Generator

This Python script defines a function for generating Pascal's triangle, which can be imported and used in a main module to produce a mathematical pattern of numbers arranged in a triangular shape.

## Usage

### Generating Pascal's Triangle

The `pascal_triangle(n)` function generates Pascal's triangle up to the **nth** row.

#### Parameters

- `n` (int): The number of rows in Pascal's triangle to generate. It should be a positive integer.

#### Importing the Function

To use the Pascal's triangle generator in your main module, import it as follows:

```python
from pascal_triangle_generator import generate_pascal_triangle

from pascal_triangle_generator import generate_pascal_triangle

def main():
    triangle = generate_pascal_triangle(5)
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()

```

#### Output

```bash
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
