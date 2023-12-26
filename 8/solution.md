# Problem 8

[Problem link](https://adventofcode.com/2023/day/8)

## Part 1

**Problem Statement**: Given a graph where every vertex has outdegree 1, find how many steps are required to reach an `end` vertex from a `start` vertex?

**Solution**: Keep moving to the (only) next vertex until we reach the target.

[**Code**](1.py)

## Part 2

**Problem Statement**: In the same graph, if you start simultaneously from `n` different vertices and keep moving to the next vertex in each of them, find how many steps are required before all of them simultaneously reach vertices satisfying a certain condition?

**Solution**: Direct simulation would take too long. Using properties of single-outdegree graphs, we can show that every start vertex would end in a cycle. For general data, we would need to use [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) based on the positions and lengths of these cycles to find the simultaneous condition. Fortunately, the test data was such that all the start vertices were at the starting points of the cycles, so we just need to take the lcm of the cycle sizes.

[**Code**](2.py)

