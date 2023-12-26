# Problem 19

[Problem link](https://adventofcode.com/2023/day/19)

## Part 1

**Problem Statement**: Given products, each of which is an `(x, m, a, s)` 4-tuple, and a workflow which moves from state to state depending on one of the values in the 4-tuple, find whether the workflow accepts or rejects each product.

**Solution**: Simulate the workflow using python `eval` to check whether the state transition conditions are satisfied.

[**Code**](1.py)

## Part 2

**Problem Statement**: For all possible 4-tuples with each value ranging from 1 to 4000, find how many of them will be accepted.

**Solution**: Trying out all 4-tuples would be too slow. Instead, we can use the same idea as we used in [Problem 5](../5/solution.md) to treat the product space as a 4-dimensional hypercuboid with each dimension an interval. Running the entire product space through the workflow will split it into smaller hypercuboids at each decision step. Keep going until we reach accept/reject states and sum up the volumes of the accepted hypercuboids.

[**Code**](2.py)

