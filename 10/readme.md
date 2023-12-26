# Problem 10

[Problem link](https://adventofcode.com/2023/day/10)

## Part 1

**Problem Statement**: Given a grid in which every cell can be connected to up to two of its neighbours, find the length of the loop containing a given cell.

**Solution**: Use [disjoint set union](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) to merge connected cells, and count the number of cells in the component of the start vertex. For more problems of this type, check the problems tagged [Disjoint Set Union](https://github.com/razimantv/leetcode-solutions#disjoint-set-union) in my [Leetcode repository](https://github.com/razimantv/leetcode-solutions).

[**Code**](1.py)

## Part 2

**Problem Statement**: Find the number of cells enclosed in this loop.

**Solution**: This was a fun problem. For each cell, we need to check efficiently whether it is inside or outside the loop. We can do this by scanning from the left and checking how many times we cross the boundary. If there were only vertical and horizontal walls, this would be easy (Every time you cross a vertical wall, toggle whether we are outside or inside the loop). But corners make things tricky. Here is one way to take care of it: Keep a counter variable. Increment it by 2 on seeing a vertical boundary, 1 on seeing a top left or bottom right corner, and on 3 on seeing a top right or bottom left corner. We are inside the loop if and only if the counter variable leaves a remainder of 2 on division by 4. Magic!

[**Code**](2.py)

