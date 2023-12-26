# Problem 5

[Problem link](https://adventofcode.com/2023/day/5)

## Part 1

**Problem Statement**: A mapping `f_i` is a set of pairs of intervals `p_ik = ((l_ik, r_ik), (L_ik, R_ik))` such that if x falls in `[l_ik, r_ik]` it is mapped linearly to `[L_ik, R_ik]`. For some given values of `x`, find the final result if `n` such mappings are applied one after the other to x.

**Solution**: In each map, loop through the interval pairs. If the current value of `x` falls in the left interval, map it to the right interval. Could be sped up with binary search, but wasn't necessary for the constraints of the problem.

[**Code**](1.py)

## Part 2

**Problem Statement**: Same as the above, but with `x` now specified as intervals instead of values.

**Solution**: Trying every number in the interval would be too slow. So find intersections and differences of each interval with the mapping intervals instead. For more problems where this idea is applied, look at problems tagged [Interval overlap](https://github.com/razimantv/leetcode-solutions#overlap) in my [Leetcode solutions repositiory](https://github.com/razimantv/leetcode-solutions).

[**Code**](2.py)

