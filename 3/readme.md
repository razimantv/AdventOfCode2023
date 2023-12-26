# Problem 3

[Problem link](https://adventofcode.com/2023/day/3)

## Part 1

**Problem Statement**: In a grid of digits and symbols, find all numbers (consecutive digits) which are adjacent horizontally, vertically or diagonally to a symbol.

**Solution**. Find the positions (rows, column ranges) of all numbers. For each number, check whether the adjacent cells (column range above and below, character before and after) have a symbol.

[**Code**](1.py)

## Part 2

**Problem Statement**: In the grid, find every pair of numbers that are adjacent to the same `*` symbol.

**Solution**: After finding the number positions as above, fr every `*` in the grid, loop over all numbers to check if they are adjacent to it.

This step can be sped up with some binary search, but it was not necessary for the problem constraints.

[**Code**](2.py)

