# Problem 6

[Problem link](https://adventofcode.com/2023/day/6)

## Part 1, 2

**Problem Statement**: Find the values of `t` in `[0, T]` such that `t (T - t)` is at least `D`.

**Solution**: Just loop over values of `t`. Could be sped up with binary search after noting that the target is a quadratic with minimum at `t = T / 2`, but wasn't necessary for the constraints.

[**Code 1**](1.py) [**Code 2**](2.py)

