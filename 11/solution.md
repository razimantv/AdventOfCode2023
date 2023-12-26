# Problem 11

[Problem link](https://adventofcode.com/2023/day/11)

## Part 1, 2

**Problem Statement**: Given a grid containing galaxies (`#`) and empty space (`.`), find the sum of manhattan distances between every pair of galaxies if every row/column without galaxies is stretched by a factor.

**Solution**: Assign a modified position to each row/column such that the position is the position of the previous row/column incremented by 1 or the stretched distance depending on whether the previous row/column contains a galaxy or not. Then find pairwise manhattan distances on these modified positions.

The solution is of quadratic complexity in the number of galaxies, and can be improved by using a segment tree. That was not required for the problem constraints.

[**Code 1**](1.py), [**Code 2**](2.py)

