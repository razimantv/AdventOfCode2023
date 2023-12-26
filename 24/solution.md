# Problem 24

[Problem link](https://adventofcode.com/2023/day/24)

## Part 1

**Problem Statement**: Given constant-velocity straight line trajectories of particles in 3D space, find how many pairs of their 2D projections intersect within a given area.

**Solution**: For every pair, use coordinate geometry to find the intersection point and check whether it has the right coordinates.

[**Code**](1.py)

## Part 2

**Problem Statement**: Find a constant-velocity straight line trajectory that will collide with all the particles.

**Solution**: We have 6 unknowns: 3 coordinates and 3 velocity components. For every intersection with a particle, we get an additional unknown (intersection time). Solving simultaneously for 3 particles gives us a system of 9 equations (one per coordinate for each particle) and 9 unknowns. Unfortunately the equation is nonlinear, so use Sage to solve it.

[**Code**](2.py)

