# Problem 21

[Problem link](https://adventofcode.com/2023/day/21)

## Part 1

**Problem Statement**: Given a grid with obstacles and a starting location, find the number of cells in the grid that can be reached in exactly S steps if you are allowed to visit the same cell twice.

**Solution**: Simulate. From all cells reachable in `i` steps, move in all 4 directions to find cells reachable in `i+1` steps. Avoid duplicates using a set.

[**Code**](1.py)

## Part 2

**Problem Statement**: Same as the above, except that the grid is now repeated infinitely periodically and the step count is much larger.

**Solution**: Simulation would no longer work. This was a problem where you had to look at the test data to notice that vertical and horizontal directions from the starting point had no obstacles, and neither did the rows and columns at the boundary. This meant that all cells within a large diamond of repeating grids were reachable (as long as they had the right parity of minimum distance within the original grid). We could use the minimum distances within the starting grid (without repetitions) found using a breadth-first search to find the reachable cells in the copies of the grid on the boundary of the diamond.

[**Code**](2.py)

