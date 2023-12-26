# Problem 23

[Problem link](https://adventofcode.com/2023/day/23)

## Part 1

**Problem Statement**: In a grid with empty cells `.`, obstacles `#`, and steep slopes `v^<>` (where your next step is forced), find the longest path from a source cell to a destination cell if you are not allowed to revisit cells.

**Solution**: Surprisingle, naive backtracking was enough for the graph.

[**Code**](1.py)

## Part 2

**Problem Statement**: Same as above, except for treating steep slopes as normal cells.

**Solution**: Backtracking was no longer feasible. But looking at the test data makes it clear that most of the cells offer no choice: there is only one direction to move to. Making a modified graph with the other cells ("junctions") as nodes and the distances between them as edges, we can perform backtracking on the modified graph to find the answer.

[**Code**](2.py)

