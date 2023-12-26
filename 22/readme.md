# Problem 22

[Problem link](https://adventofcode.com/2023/day/22)

## Part 1

**Problem Statement**: Given axis-aligned cuboids that are falling down to rest at the bottom or on top of other cuboids (ignoring rotational stability). Find the number of cuboids which end up being the only cuboid to support another cuboid.

**Solution**: Sort the cuboids by starting vertical position and process them one by one. For every cell in the planar projection of the cuboid being processed, find the highest cell in an already processed cuboid. If all such cells at the highest point belong to the same cuboid, then it is the unique supporting cuboid. Find all such cuboids.

[**Code**](1.py)

## Part 2

**Problem Statement**: For each cuboid, find how many other cuboids will fall if it were removed.

**Solution**: Simulate. Find the vertical positions of all cuboids in the original arrangement. For every cuboid, remove it and recalculate the positions. The cuboids that fall are exactly those whose positions have changed compared to the original arrangement.

[**Code**](2.py)

