# Problem 12

[Problem link](https://adventofcode.com/2023/day/12)

## Part 1

**Problem Statement**: Given a string `s` with `.#?` characters and a list `l` of numbers, find the number of ways to replace the `?` characters with `.` and `#` such that the counts of consecutive `#` characters form the given list.

**Solution**: For this part, the constraints were small so that we could brute force all the `2^Q` ways of assigning the `Q` `?` characters and check whether the string was valid.

[**Code**](1.py)

## Part 2

**Problem Statement**: Same as above, but the strings and lists are now too big to allow brute force enumeration.

**Solution**: Use dynamic programming. Define `f(i, j)` to be the number of ways of assigning the characters of string starting from character `i` such that the consecutive `#` characters in this suffix are equal to the list elements starting with position `j`. Then `f(0, 0)` is what we need to find. The recurrence relation is straightforward. If the `i`th character is `.` or `?`, then `f(i, j)` gets a contribution of `f(i+1, j)`. If the substring starts with `l[j]`  `#` characters followed by a non-`#` character, `f(i, j)` gets a contribution of `f(i + l[j] + 1, j + 1)`. Adding the base cases and using memoised recursion gives us the solution

[**Code**](2.py)

