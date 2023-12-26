# Problem 14

[Problem link](https://adventofcode.com/2023/day/14)

## Part 1

**Problem Statement**: Given a grid of `#` (obstacles), `O` (movable objects) and `.` (empty space), find out where all the `O` characters end up if they all move north.

**Solution**: Transpose the grid and sort the substrings between `#` characters and join them again.

[**Code**](1.py)

## Part 2

**Problem Statement**: Make the objects move north, west, south and east one after the other, and repeat this process 10^9 times.

**Solution**: Direct simulation would be too slow. But notice that the states of the grid form a single-outdegree graph as in [Problem 8](../8/solution.md). So we are guaranteed to hit a cycle. Just simulate (with the help of numpy to simplify the implementation) and remember the states until we enter the cycle, and predicting the state afterwards is easy.

[**Code**](2.py)

