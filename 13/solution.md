# Problem 13

[Problem link](https://adventofcode.com/2023/day/13)

## Part 1

**Problem Statement**: Given a grid of `.#` characters, find vertical and horizontal lines of mirror symmetry - that is, horizontal or vertical lines such that all cells to the two sides of the line are identical (up to the boundary of the grid).

**Solution**: Just check every horizontal and vertical line. Use numpy to simplify the evaluation.

[**Code**](1.py)

## Part 2

**Problem Statement**: Find a cell in the grid such that flipping its value causes a new horizontal/vertical symmetry line to emerge.

**Solution**: Surprisingly, it was enough to just loop through every cell and repeat the above process. A better solution would be to make one pass through all the possible symmetry lines and find the ones that have exactly one mismatch, but that improvement was not required here.

[**Code**](2.py)

