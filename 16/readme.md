# Problem 16

[Problem link](https://adventofcode.com/2023/day/16)

## Part 1

**Problem Statement**: Given a grid with empty space `.`, mirrors `\/` and splitters `-|`, find how many cells light will pass through if inserted at a point.

**Solution**: [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search), but remember to set the state to be the combination of position and direction.

[**Code**](1.py)

## Part 2

**Problem Statement**: Find the point of insertion of light that will make it pass through the maximum number of cells.

**Solution**: It is quick enough to repeat the above procedure from every starting point.

[**Code**](2.py)

