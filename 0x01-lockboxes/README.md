# Box Unlocker

This Python module contains a function to determine if all the boxes in a list can be opened by following the keys stored within each box.

## Function: `canUnlockAll(boxes)`

- Determines if all boxes can be opened starting from the first box.

### Parameters:

- `boxes` (list of lists): A list of boxes, each containing keys to other boxes.

### Returns:

- `True` if all boxes can be opened, `False` otherwise.

Example usage:

```python
from lockboxes import canUnlockAll

# All boxes can be unlocked because each box contains keys to other boxes.
boxes = [[1, 2], [3], [0], []]
print(canUnlockAll(boxes)) # Output will be True.

# All boxes can be unlocked because each box contains keys to other boxes.
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # Output will be True.

# Not all boxes can be unlocked because there is a circular dependency.
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # Output will be False
```
