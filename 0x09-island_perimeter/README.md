# 0x09. Island Perimeter

This task requires the calculation of the perimeter of an island described in a grid, and the following steps can be taken to provide the challenge's resolution:

## Step 1: Create the script

```bash
$ touch 0-island_perimeter.py
$ chmod x+ 0-island_perimeter.py
```

## Step 2: Understanding the Problem

1. The grid represents an island where 0 represents water and 1 represents land.

2. Find the perimeter of the island.

3. The island doesn't have "lakes", this means the water inside isn't connected to the water surrounding the island.

4. The grid is rectangular in shape, and its width and height do not exceed 100.

## Step 3: Plan the Implementation

1. Loop through each cell in the grid.

2. For each land cell (where the value is 1), check its surroundings (up, down, left, right).

3. Increment the perimeter for each boundary the land cell shares with water (0).

4. Make sure to handle edge cases (cells on the boundary of the grid).

## Step 4: Write the code

```bash
def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check down
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
```

## Step 5: Run the main script

After completing the function definition, run a test by executing main module `0-main.py` where the source code's functionality is imported for confirmation:

```
$ ./0-main.py
```

**Expected Output:**

```bash
$ ./0-main.py
12
```

## Explanation

The land cells at positions (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), and (4, 1) contribute to the perimeter, resulting in a total perimeter of 12.
