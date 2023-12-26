# Problem 17

[Problem link](https://adventofcode.com/2023/day/17)

## Part 1, 2

**Problem Statement**: Find the shortest path from the top left to bottom right in a weighted grid if there are lower and upper limits on how many straight steps you can take before a turn.

**Solution**: [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) where the state is the current position combined with the current direction and the number of steps we have moved in the direction.

[**Code 1**](1.py), [**Code 2**](2.py)

