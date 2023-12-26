# Problem 18

[Problem link](https://adventofcode.com/2023/day/18)

## Part 1, 2

**Problem Statement**: Given a loop in the 2D plane, expressed as piecewise up/down/left/right lines, find its enclosed area.

**Solution**: A bit like an extension of [Problem 10](../10/solution.md). The idea here was to treat it as an integration problem. If we kept an area variable, adding `y * L` while moving right and subtracting `y * L` while moving left, that would amount to an integral of `y dx`, providing the area of the loop. Add 1 + half the length of the loop to take care of the boundary.

[**Code 1**](1.py), [**Code 2**](2.py)

